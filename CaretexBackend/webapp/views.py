from django.shortcuts import render, HttpResponse
import datetime
# TO send messages
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("This is Home Page")
    # return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("This is Contact Page")

def services(request):
    return HttpResponse("This is Services Page")