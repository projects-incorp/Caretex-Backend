from django.contrib import admin
from . import models
from .models import Products, AllOrders

# Register your models here.
admin.site.register(Products)
admin.site.register(AllOrders)
