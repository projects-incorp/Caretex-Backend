from rest_framework import serializers
from . import models

class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = ('title', 'size')
