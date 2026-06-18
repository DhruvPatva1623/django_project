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
    d = ""
    if c == 30:
        d = "If condition called"
    elif c<30:
        d = "Elif condition less than"
    else:
        d = "Else condition"
    
    #return HttpResponse(msg)
    return render(request, 'ans.html',{'mya':a,'myb':b,'myc':c,'myd':d})

# def marksheet(request):
#     a = int(request.POST[ 'sub1' ])
#     b = int(request.POST[ 'sub2' ])
#     c = int(request.POST[ 'sub3' ])
#     d = int(request.POST[ 'sub4' ])
#     e = int(request.POST[ 'sub4' ])
#     print(a, b, c, d, e)
#     t = a + b + c + d + e 
#     total = "Total =",t
#     g = ((t / 500 )* 100)
#     grade = "grade =" ,g,"%" 
#     if g>50:
#         print("pass")
#     return render(request,"marks.html", {"mys":a })

def saveSessionData(request):
    request.session['username'] = "Dhruv Patva \n savedSessionData"
    return HttpResponse("Session created")

def getSessionData(request):
    msg = request.session['username']
    return HttpResponse(msg)


# Create your views here.
