from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

# def contac(request):
#     if request.method == 'GET':
#         return render(request, 'app/data.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных формы
        return HttpResponse(f"Данные отправлены!{name}")
    return render(request, 'catalog/contact.html')



