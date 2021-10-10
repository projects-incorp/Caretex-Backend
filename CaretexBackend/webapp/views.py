from django.shortcuts import render, HttpResponse, redirect
import datetime
from rest_framework import generics
from . import serializers, models
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
# TO send messages
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse("This is Home Page")
    # return HttpResponse("This is Home Page")

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

def logoutUser(self):
    logout(request)
    #redirect to login page
    return redirect("")


def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("This is Contact Page")

def services(request):
    return HttpResponse("This is Services Page")

class Products(generics.ListAPIView):
    serializer_class = serializers.ProductList
    queryset = models.Products.objects.all()
