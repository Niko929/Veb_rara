from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('new_cot/', views.new_cot, name='new_cot'),
    path('', views.home, name='home'),


]