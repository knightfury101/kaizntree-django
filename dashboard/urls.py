# urls.py
from django.urls import path
from .views import list_products, create_product, category_list, tag_list

urlpatterns = [
    path('products/', create_product, name='create_product'),
    path('categories/', category_list, name='category_list'),
    path('tags/', tag_list, name='tag_list'),
    path('filter/', list_products, name='list_products')
]
