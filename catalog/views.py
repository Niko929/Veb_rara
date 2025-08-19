from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pyexpat.errors import messages
from .models import Product
from .forms import ProductForm, StyleFormMixin, ModeratorForm
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

class MenuView(ListView):
    model = Product
    template_name = 'catalog/menu.html'
    context_object_name = 'product'


class ContactView(View):
    template_name = 'catalog/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Данные отправлены!{name}")

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_product_list(self):
        # Попытка получить данные из кеша
        data = cache.get('my_key')
        # Если данные не найдены в кеше, выполняем вычисления и сохраняем результат в кеш
        if not data:
            fertd = super().get_product_list()
            cache.set('my_key', fertd, 60 * 15)  # Кешируем данные на 15 минут
        # Возвращаем ответ с данными
        return HttpResponse(data)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    login_url = '/users/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class ProductCreateView(LoginRequiredMixin ,CreateView):
    login_url = '/users/login/'
    redirect_field_name = 'next'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = '/products/'  # или используйте get_success_url

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Товар успешно создан!')
        return response

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/users/login/'
    redirect_field_name = 'next'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = '/products/'  # или используйте get_success_url

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Изменения сохранены успешно!')
        return response

    def get_form_class(self):
        user = self.request.user
        if user == self.object.categoru:
            return StyleFormMixin
        if user.has_perm("Product.can_review_categoru") and user.has_perm("Product.can_recommend_categoru"):
            return ModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    login_url = '/users/login/'
    redirect_field_name = 'next'
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    context_object_name = 'product'




@login_required(login_url='/users/login/')
def product_detail(request, pk):
    """
    Представление для просмотра деталей продукта.
    Доступно только авторизованным пользователям.
    """
    # Получаем продукт или возвращаем 404 если не найден
    product = get_object_or_404(Product, pk=pk)

    # Контекст для передачи данных в шаблон
    context = {
        'product': product,
        'is_staff': request.user.is_staff  # Проверка прав администратора
    }

    return render(request, 'catalog/product_detail.html', context)