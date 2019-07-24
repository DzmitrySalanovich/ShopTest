from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey(to='self', blank=True, null=True, on_delete=models.SET_NULL, related_name="subcategories")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    sku = models.IntegerField()
    discount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ManyToManyField(to=Category, related_name='products')

    def __str__(self):
        return self.name

class Product_att(models.Model):
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=10)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return self.name
