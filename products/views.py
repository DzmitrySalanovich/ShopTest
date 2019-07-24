from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Category, Product, Product_att
from .serializers import CategorySerializer, ProductSerializer, Product_attSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import filters


class ProductFilter(FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
        
    @action(detail=True, methods=['get'])
    def subcategories(self, request, *args, **kwargs):
        self.queryset = self.get_object().subcategories.all()
        return self.list(request)