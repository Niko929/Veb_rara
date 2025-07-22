from django.urls import path
from . import views
from .views import HomeView, ContactView, NewCotView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('new_cot/', NewCotView.as_view(), name='new_cot'),
]