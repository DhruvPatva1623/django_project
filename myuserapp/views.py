from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepageview(request):
    return render(request, "home.html")

def aboutpageview(request):
    return render(request, "about.html")

def contactpageview(request):
    return render(request, "contact.html")

def hello(request):
    return render(request, "hello.html")

# Create your views here.
