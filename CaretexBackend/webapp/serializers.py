from rest_framework import serializers
from . import models 

class ProductList(serializers.ModelSerializer):
    class Meta:
        model = models.AllOrders
        fields = '__all__'