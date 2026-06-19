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

    path('contactprocess',views.contactprocess),
    # path('markprocess')
    path('saveSession',views.saveSessionData),
    path('getSessionData',views.getSessionData),
    path('getSessionData1',views.getSessionData1),
    path('removedSession',views.deleteSessionData1),

    path('login',views.loginpage),
    path('loginprocess',views.loginprocess),
    path('dashboard',views.dashboard),
    path('logout',views.logout),

    path('mailsenddemo',views.mailsenddemo),
    path('dynamicmail',views.dynamicmailpage),
    path('mailProcess',views.dynamicmailprocess)
]