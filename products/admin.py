from django.contrib import admin
from products.models import Category, Product, Product_att

@admin.register(Product_att)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class Product_attAdmin(admin.ModelAdmin):
    pass