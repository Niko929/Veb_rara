from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView, ContactView, MenuView, ProductUpdateView, \
    ProductDeleteView, ProductCreateView, product_detail
app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', ProductListView.as_view(), name='product_list'),  # New list view
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path("menu/", MenuView.as_view(), name='menu'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/manage/', product_detail, name='product_manage'),
]
