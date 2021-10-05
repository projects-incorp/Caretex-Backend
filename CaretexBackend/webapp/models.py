from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=200, blank=False)
    size=models.CharField(max_length=100, blank=True)
