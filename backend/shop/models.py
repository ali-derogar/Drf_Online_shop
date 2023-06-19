from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True , blank=True ,default=None, on_delete=models.CASCADE ,related_name='child')

    
    def __str__(self):
            return self.name

class Product(models.Model):
    model = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    number = models.IntegerField()
    status = models.BooleanField(default=True)
    parent = models.ForeignKey(Category , null=True , blank=True , default=None,on_delete=models.CASCADE,related_name='product')
    
    def __str__(self):
            return self.model
        
class Cart(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True , blank=True ,default=None,related_name='cart')
    product = models.ManyToManyField(Product , null=True , blank=True ,related_name='cart')
    def __str__(self):
            return self.name