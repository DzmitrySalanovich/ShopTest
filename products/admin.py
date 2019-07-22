from django.contrib import admin
from products.models import Category, Product, Product_att

class CategoryAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class Product_attAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Product_att, Product_attAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
