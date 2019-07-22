from django.contrib import admin
from orders.models import Order, LineItem

@admin.register(LineItem)
class OrderAdmin(admin.ModelAdmin):
    pass  

@admin.register(Order)
class LineItemAdmin(admin.ModelAdmin):
    pass