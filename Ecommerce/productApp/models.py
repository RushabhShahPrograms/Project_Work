from unicodedata import category
from django.db import models
from django.urls import reverse

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