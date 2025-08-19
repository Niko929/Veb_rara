from django.core.cache import cache
from .models import Product, Category


def get_products_by_category(category_slug):
    """
    Возвращает список продуктов в указанной категории
    с использованием кеширования
    """
    cache_key = f'products_category_{category_slug}'
    products = cache.get(cache_key)

    if products is None:
        try:
            category = Category.objects.get(slug=category_slug)
            products = Product.objects.filter(category=category, is_active=True).select_related('category')
            cache.set(cache_key, products, 60 * 15)  # Кешируем на 15 минут
        except Category.DoesNotExist:
            products = []

    return products