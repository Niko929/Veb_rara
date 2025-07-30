from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView
from django.views.generic import FormView
from django import forms
from django.views.generic import TemplateView


# class HomeView(ListView):
#     model = Product
#     template_name = 'catalog/home.html'
#     context_object_name = 'products'
def home(request):
    products = Product.objects.all()
    # Передаем товары в шаблон
    context = {
        'products': products
    }
    return render(request, 'catalog/home.html',context)

def new_menu(request):
    product = Product.objects.all()
    return render(request, 'catalog/menu.html', {'product': product})



#
# class ContactForm(forms.Form):
#     name = forms.CharField(label='Ваше имя')
#     message = forms.CharField(widget=forms.Textarea, label='Сообщение')
#
#
# class ContactView(FormView):
#     template_name = 'catalog/contact.html'
#     form_class = ContactForm
#     success_url = '/'  # URL для перенаправления после успешной отправки
#
#     def form_valid(self, form):
#         name = form.cleaned_data['name']
#         message = form.cleaned_data['message']
#         # Здесь можно добавить обработку данных (например, отправка email)
#         return HttpResponse(f"Данные отправлены! {name}")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных формы
        return HttpResponse(f"Данные отправлены!{name}")
    return render(request, 'catalog/contact.html')


# class NewCotView(TemplateView):
#     template_name = 'catalog/new_cot.html'
def new_cot(request):
    return render(request, 'catalog/new_cot.html')

def product_detail(request, product_id):  # Имя параметра должно совпадать с URL
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_list.html', {'product': product})

def contacts(request):
    return render(request, 'catalog/contact.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/menu.html', {'products': products})
