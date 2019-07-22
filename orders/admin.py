from django.contrib import admin
from orders.models import Order, LineItem

class OrderAdmin(admin.ModelAdmin):
    pass  

class LineItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(LineItem, LineItemAdmin)
admin.site.register(Order, OrderAdmin)