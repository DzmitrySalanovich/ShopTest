from django.db import models
from authentication.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    AVAILABLE = 'AV'
    IN_PROGRESS = 'INPR'
    COMPLITE = 'CMP'
    STATUSES = [
        (AVAILABLE, 'Available'),
        (IN_PROGRESS, 'In progress'),
        (COMPLITE, 'Complite'),
    ]
    user = models.ForeignKey(to=User, on_delete = models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    cc_number = models.CharField(max_length=15)
    status = models.CharField(choices=STATUSES, max_length=100)


class LineItem(models.Model):
    product_sku = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    datatime = models.DateTimeField('date ordered')
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)