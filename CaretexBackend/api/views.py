from django.shortcuts import render

# Create your views here.
from rest_framework import generics 
from . import serializers, models 
class ShopItemList(generics.ListAPIView): 
    serializer_class = serializers.ShopItemSerializer 
    queryset = models.ShopItem.objects.all()
