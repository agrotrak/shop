__author__ = 'dl'
from django.db import models

# Create your models here.

__action_type={'view_category':1,'view_product':2,'add_to_basket':3,'del_from_basket':4,'buy':5,'login':6,'logout':7}

class Category(models.Model):
    id1c=models.IntegerField()
    name=models.CharField(max_length=100)
    parent=models.IntegerField()

class Product(models.Model):
    id1c=models.IntegerField()
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category)
    count=models.IntegerField()
    cost=models.FloatField()

class Order(models.Model):
    owner=models.CharField(max_length=100)
    info=models.ManyToManyField(Product,through='OrderInfo')
    date=models.DateTimeField()
    total=models.IntegerField()

class OrderInfo(models.Model):
    product=models.ForeignKey(Product)
    order=models.ForeignKey(Order)
    count=models.IntegerField()

