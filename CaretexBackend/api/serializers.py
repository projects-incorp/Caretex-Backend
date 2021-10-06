from rest_framework import serializers 
from api.models import ShopItem

class ShopItemSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ShopItem 
        fields = ('title', 'quantity', 'description', 'category')