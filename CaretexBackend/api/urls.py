from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.ShopItemList.as_view()), 
]