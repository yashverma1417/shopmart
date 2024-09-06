from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=20)
   seller_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='seller_id')

class Product(models.Model):
   seller_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='seller_id')
   name = models.CharField(max_length=25)
   price=models.FloatField()
   category_id = models.ForeignKey(Category,on_delete=models.CASCADE,db_column='category_id')
   description=models.CharField(max_length=100)
   quantity=models.IntegerField()
   is_active=models.BooleanField()
   image=models.ImageField(upload_to='image')
   
   

   

   
