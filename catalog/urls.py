from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView, ContactView, MenuView

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view, name='home'),
    path('products/', ProductListView.as_view, name='product_list'),  # New list view
    path('products/<int:product_id>/', ProductDetailView.as_view, name='product_detail'),
    path('contacts/', ContactView.as_view, name='contacts'),
    path("menu/", MenuView.as_view, name='menu')
]