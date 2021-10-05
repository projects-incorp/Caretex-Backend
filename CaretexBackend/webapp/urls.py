from django.contrib import admin
from django.urls import path, include
from webapp import views
from django.conf.urls import url

urlpatterns = [
    #path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    url(r'^$', views.ProductItemList.as_view()),

]
