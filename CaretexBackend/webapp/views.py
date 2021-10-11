from django import forms
from django.shortcuts import render, HttpResponse, redirect
import datetime
from rest_framework import generics
from . import serializers, models, forms
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
# TO send messages
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse("This is Home Page")

#Register User
def signup(request):
    register = forms.CreateUser()
    if request.method == 'POST':
        forms.CreateUser(request.POST)
        if register.is_valid():
            register.save()
            return redirect('/')
    return render(request, '/')

# Login User
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        
        else:
            #login page
            return render(request, '/')
    #login page
    return render(request, '/')

# Logout User
def logoutUser(request):
    #redirect to login page
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, '/')




def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("This is Contact Page")

def services(request):
    return HttpResponse("This is Services Page")

class Products(generics.ListAPIView):
    serializer_class = serializers.ProductList
    queryset = models.Products.objects.all()
