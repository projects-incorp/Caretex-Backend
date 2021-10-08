from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    GTIN=models.BigIntegerField()
    code=models.CharField(max_length=25)
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=700)
    mrp=models.FloatField()
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class AllOrders(models.Model):
    amount=models.FloatField()
    product=models.ManyToManyField(Products)