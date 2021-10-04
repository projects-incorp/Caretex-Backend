from django.contrib import admin
from . import models

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'id', 'quantity')

admin.site.register(models.Inventory, InventoryAdmin)