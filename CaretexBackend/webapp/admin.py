from django.contrib import admin
from .models import Products

# Register your models here.
#ProductsAdmin(admin.ModelAdmin)
#list_display = ('title', 'size')
admin.site.register(Products)
