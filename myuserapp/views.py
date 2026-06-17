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
def shop(request):
    return render(request,"shop.html")
def contactprocess(request):
    a = int(request.POST[ 'txt1' ])
    b = int(request.POST[ 'txt2' ])
    c = a + b
    msg = " a = ",a," b = ",b," sum =",c 
    
    return HttpResponse(msg)
# Create your views here.
