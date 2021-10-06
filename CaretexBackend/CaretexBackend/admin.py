# Register your models here.
from django.contrib import admin 
from . import ShopItem


list_display = ('id', 'title', 'category') 
admin.site.register(ShopItem)