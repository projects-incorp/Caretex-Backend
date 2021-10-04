from rest_framework import serializers, generics
from . import models 

class ProductList(serializers.ModelSerializer):
    class Meta:
        model = models.Inventory
        fields = ('name', 'cost', 'id', 'quantity')

    