from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('api', views.Products.as_view(), name="api"),
    path('signup', views.signup, name="signup"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
]