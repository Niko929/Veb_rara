from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView
from django.views.generic import FormView
from django import forms
from django.views.generic import TemplateView



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


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных формы
        return HttpResponse(f"Данные отправлены!{name}")
    return render(request, 'catalog/contact.html')


def new_cot(request):
    return render(request, 'catalog/product_list.html')

def product_detail(request, product_id):  # Имя параметра должно совпадать с URL
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})

def contacts(request):
    return render(request, 'catalog/contact.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/menu.html', {'products': products})
