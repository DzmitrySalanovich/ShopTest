from django.contrib import admin
from products.models import Category, Product, Product_att

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class Product_attAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product_att, Product_attAdmin)
