from rest_framework import serializers 
from . import models 
class ShopItemSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = models.ShopItem 
        fields = ('title', 'quantity', 'description', 'category')