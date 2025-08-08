from django.urls import path
from catalog import views
from .views import HomeView, ProductListView, ProductDetailView, ContactView, MenuView

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view, name='product_list'),  # New list view
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path("menu/", MenuView.as_view(), name='menu'),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
]