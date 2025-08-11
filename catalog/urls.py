from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView, ContactView, MenuView, ProductUpdateView, \
    ProductDeleteView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),  # New list view
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path("menu/", MenuView.as_view(), name='menu'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]