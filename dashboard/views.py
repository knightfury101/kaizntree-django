from django.shortcuts import render

# views.py
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Product, Category, Tag
from .serializers import ProductSerializer, CategorySerializer, TagSerializer
from drf_yasg.utils import swagger_auto_schema
from kaizntree_backend.Constants import *
from .schemas import list_products_parameters


@swagger_auto_schema(method='post', 
                     operation_description = "Make a product", 
                     request_body=ProductSerializer, 
                     tags = [PRODUCT])  

@api_view(['POST', 'GET'])
@permission_classes([permissions.IsAuthenticated])
def create_product(request):
    if request.method == 'GET':
        user = request.user  # Assuming user authentication is enabled
        products = Product.objects.filter(user=user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', 
                     operation_description = "Define A Category", 
                     request_body=CategorySerializer, 
                     tags = [PRODUCT])  


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def category_list(request):
    print(request.user)
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='post', 
                     operation_description = "Define A Tag", 
                     request_body=TagSerializer, 
                     tags = [PRODUCT])  


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', 
                     operation_description = "Sort and Filter Products", 
                     manual_parameters=list_products_parameters, 
                     tags = [PRODUCT])         
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_products(request):
    name_contains = request.GET.get('name_contains', '')
    category = request.GET.get('category', '')
    tags = request.GET.getlist('tags')
    stock_status_min = request.GET.get('stock_status_min', None)
    stock_status_max = request.GET.get('stock_status_max', None)
    available_stock_min = request.GET.get('available_stock_min', None)
    available_stock_max = request.GET.get('available_stock_max', None)

    # Query products based on filtering parameters
    products = Product.objects.filter(user=request.user)
    if name_contains:
        products = products.filter(name__icontains=name_contains)
    if category:
        products = products.filter(category__name=category)
    if tags:
        products = products.filter(tags__tag_title__in=tags)
    if stock_status_min is not None:
        products = products.filter(stock_status__gte=stock_status_min)
    if stock_status_max is not None:
        products = products.filter(stock_status__lte=stock_status_max)
    if available_stock_min is not None:
        products = products.filter(available_stock__gte=available_stock_min)
    if available_stock_max is not None:
        products = products.filter(available_stock__lte=available_stock_max)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)    