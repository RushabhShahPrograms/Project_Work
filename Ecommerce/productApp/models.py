from itertools import product
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.urls import reverse
from userApp.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        db_table = "category"
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=25)
    product_price = models.FloatField()
    product_qty = models.IntegerField()
    product_desc = models.TextField()
    product_available_count = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to='images/', null=True)
    product_creation_date = models.DateTimeField()
    product_availablity = models.BooleanField(null=True)
    product_is_featured = models.BooleanField(default=False)

    #product_Product
    class Meta:
        db_table = "product"

    def __str__(self):
        return self.product_name

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"

    def get_total_item_price(self):
        return self.quantity * self.product.product_price

    def get_final_price(self):
        return self.get_total_item_price()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, unique=True,default=None, blank=True,null=True)
    datetime_ofpayment = models.DateTimeField(auto_now_add=True)
    order_delivered = models.BooleanField(default=False)
    order_received = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.datetime_ofpayment and self.pk:
            self.order_id = self.datetime_ofpayment.strftime('PAY2ME%Y%m%dODR') + str(self.pk)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total=0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def get_total_count(self):
        order = Order.objects.get(pk=self.pk)
        return order.items.count()


class Demo(models.Model):
     username = models.CharField(max_length = 99, unique = True)
     profile_pic = models.ImageField(upload_to = "profile_pic")
     
     
     
     @property
     def imageURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = ''
        return url