from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()

    # Передаем товары в шаблон
    context = {
        'products': products
    }
    return render(request, 'catalog/home.html',context)



def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных формы
        return HttpResponse(f"Данные отправлены!{name}")
    return render(request, 'catalog/contact.html')


def new_cot(request):
    return render(request, 'catalog/new_cot.html')


