from rest_framework import serializers
from .models import Category, Product, Product_att


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'subcategories')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'discount', 'price', 'quantity', 'category')

class Product_attSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_att
        fields = ('id', 'name', 'product_id')
