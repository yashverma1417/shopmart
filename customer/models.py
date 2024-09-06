from django.db import models
from seller.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
   product_id=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='product_id')
   customer_id=models.ForeignKey(User,on_delete=models.CASCADE,db_column='customer_id')
   quantity = models.IntegerField()
   
class Profile(models.Model):
   user_id=models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
   contact=models.CharField(max_length=20)
   street=models.CharField(max_length=20)
   city=models.CharField(max_length=20)
   state=models.CharField(max_length=20)
   pincode=models.CharField(max_length=20)
   