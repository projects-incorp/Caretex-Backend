from django.db import models
# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=50, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=5)
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()