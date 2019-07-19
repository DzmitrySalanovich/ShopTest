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
    discount = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField()
    category = models.ManyToManyField(to=Category)

    def __str__(self):
        return self.name
        
class Product_att(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
