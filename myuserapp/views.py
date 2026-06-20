from django.shortcuts import render,redirect #added redirect for login and dashboard
from django.http import HttpResponse 
from django.core.mail import send_mail #day4 for mail
from django.conf import settings #day4 for mail
from . models import student #day 5
#day 6 auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def menu(request):
    return render(request,"menu.html")

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

#day 3 session management

def saveSessionData(request):
    request.session['username'] = "Dhruv Patva \n savedSessionData"
    request.session['age'] = "19"
    return HttpResponse("Session created")

def getSessionData(request):
    msg = request.session['username']
    return HttpResponse(msg)

def getSessionData1(request):
    if request.session.has_key('username'):
        msg = request.session['username']
        return HttpResponse(msg)
    else:
        return HttpResponse("Session Variable not present")

def deleteSessionData1(request):
    del request.session['username']
    return HttpResponse("Session Removed")

def loginpage(request):
    return render(request,"login.html")

def loginprocess(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    Password = request.POST.get('password')
    request.session['name'] = name
    request.session['email'] = email
    request.session['password'] = Password
# Fix: Redirect to the URL name 'dashboard' instead of the view function.
    return redirect('/dashboard')

def dashboard(request):
    if request.session.has_key('name') and request.session.has_key('email') and request.session.has_key('password'):
        return render(request,"dashboard.html")
    else:
        return redirect(loginpage)

def logout(request) :
    del request.session['name']
    del request.session['email']
    del request.session['password']
    return redirect(loginpage)

#day 4 mail sending

def mailsenddemo(request):
    subject = 'Mail is Sent by The Messi'
    message = 'Iss baar bhi FIFA World Cup jeetegne wala hai!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['@gmail.com']  #aalways remove before pushing to git also from setting 
    send_mail( subject, message, email_from, recipient_list) 
    return HttpResponse("Mail Dekh Lijiye Bhaiya! manual mail sent")

def dynamicmailpage(request):
    return render(request,"mail.html")  

def dynamicmailprocess(request):
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.POST.get('to'),]  #aalways remove before pushing to git also from setting 
    send_mail( subject, message, email_from, recipient_list) 
    return HttpResponse("Dynamically Mail Sent!")

#day 5 

def addstudentform(request):
    return render(request,'student-add-data.html')

def studentformprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    # Save the student once using the model's actual field names.
    student.objects.create(name=txt1, email=txt2, mobile=txt3, address=txt4)
    mymsg = f"User tried to log in. Name: {txt1}, email: {txt2}, mobile: {txt3}, address: {txt4}"
    subject = "Contact us from website"
    email_from =settings.EMAIL_HOST_USER
    message = mymsg
    recipient_list = ['@gmail.com']
    send_mail( subject, message, email_from, recipient_list)

    # Mail goes to user.
    mymsg = f"Successfully logged in! Name: {txt1}, email: {txt2}, mobile: {txt3}, address: {txt4}"
    subject = "Tried to log in website"
    email_from = settings.EMAIL_HOST_USER
    message = mymsg
    recipient_list = [txt2]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Thank you")

def studentdisplay(request):
    data = student.objects.all()
    return render(request,'student-data-display.html',{'students':data})

def deletestudent(request,id):
    student.objects.filter(id=id).delete()
    return redirect('/display-student/id')

#day 6 sign up page


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

    return render(request, 'signup_register.html')

def signup_view(request):
    return render(request, 'signup.html')

# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def home_view(request):
    return render(request, 'home.html')

@login_required(login_url='/')
def home_view(request):
    return render(request, 'home.html')
