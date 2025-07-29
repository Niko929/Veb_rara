from django.urls import path
from . import views
# from .views import HomeView, ContactView, NewCotView

app_name = 'catalog'

# urlpatterns = [
#     path('base/', views.base, name='base'),
#     path('contact/', ContactView.as_view(), name='contact'),
#     path('new_cot/', NewCotView.as_view(), name='new_cot'),
#     path('products/<int:product_id>/', views.product_detail, name='product_detail'),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path("menu/", views.new_menu, name = 'menu')
]