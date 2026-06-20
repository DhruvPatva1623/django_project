#urls.py is used to navigate through the app and project
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.homepageview),
    path('home',views.homepageview),
    path('about',views.aboutpageview),
    path('contact',views.contactpageview),
    path('hello',views.hello),
    path('shop',views.shop),
    path('menu',views.menu),

#day 2 form handling

    path('contactprocess',views.contactprocess),
    # path('markprocess')
    path('saveSession',views.saveSessionData),
    path('getSessionData',views.getSessionData),
    path('getSessionData1',views.getSessionData1),
    path('removedSession',views.deleteSessionData1),

#day 3 user authentication

    path('login',views.loginpage),
    path('loginprocess',views.loginprocess),
    path('dashboard',views.dashboard),
    path('logout',views.logout),

#day 4 mail sending

    path('mailsenddemo',views.mailsenddemo),
    path('dynamicmail',views.dynamicmailpage),
    path('mailProcess',views.dynamicmailprocess),

#day 5 database connectivity

    path('addstudent',views.addstudentform),
    path('studentprocess',views.studentformprocess),

    path('display-student',views.studentdisplay),
    path('deletestudent/<int:id>',views.deletestudent),
    
  #  path('StudentLogin',views.student_login_mail)

#day 6 for sign page

    path('signup', views.signup_view, name='signup'),
    path('signup_register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('logout-page/', views.logout_view, name='logout-page'),
]