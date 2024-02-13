# serializers.py
from rest_framework import serializers
from .models import Product, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_title']

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many = True)
    # tags = TagSerializer(many = True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Product
        fields = ['user','sku', 'name', 'category', 'tags', 'stock_status', 'available_stock']
