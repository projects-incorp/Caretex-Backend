from __future__ import unicode_literals
from django.db import models
class FeedItem(models.Model):
    title = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True) 
    style = models.CharField(max_length=100, blank=True) 
    description = models.TextField(blank=True)