from django.db import models
# from django.contrib.auth import models


# Create your models here.

class Product(models.Model):
    CAT=((1, "mobile"), (2,"shoes"), (3, "cloths"))
    name=models.CharField(max_length=50, verbose_name="Product Name")
    price=models.IntegerField()
    category=models.IntegerField(verbose_name="Category", choices=CAT)
    product_details = models.CharField(max_length=500, verbose_name="Product Details")
    is_active=models.BooleanField(default=True, verbose_name="Available")
    img=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete = models.CASCADE, db_column = 'user_id')
    pid = models.ForeignKey("Product", on_delete=models.CASCADE, db_column="pid")
    qty = models.IntegerField(default = 1)

class Order(models.Model):
    order_id = models.CharField(max_length =100)
    user_id = models.ForeignKey('auth.User', on_delete = models.CASCADE, db_column = 'user_id')
    pid = models.ForeignKey("Product", on_delete=models.CASCADE, db_column="pid")
    qty = models.IntegerField(default = 1)
    amt = models.FloatField()

class MyOrder(models.Model):
    order_id = models.CharField(max_length =100)
    user_id = models.ForeignKey('auth.User', on_delete = models.CASCADE, db_column = 'user_id')
    pid = models.ForeignKey("Product", on_delete=models.CASCADE, db_column="pid")
    qty = models.IntegerField(default = 1)
    amt = models.FloatField()