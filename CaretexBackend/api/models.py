from __future__ import unicode_literals
from django.db import models
class ShopItem(models.Model):
    title = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField() 
    category = models.CharField(max_length=100, blank=True) 
    description = models.TextField(blank=True)