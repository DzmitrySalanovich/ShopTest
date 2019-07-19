from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    category_id = models.ForeignKey(to='self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    sku = models.IntegerField()
    discount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ManyToManyField(to=Category)

    def __str__(self):
        return self.name

class Product_att(models.Model):
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=10)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return self.name
