# Register your models here.
from django.contrib import admin 
from api import models

class ShopItemAdmin(admin.ModelAdmin): 
    list_display = ('id', 'title', 'category') 
    admin.site.register(models.ShopItem, ShopItemAdmin)