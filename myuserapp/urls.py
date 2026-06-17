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
    path('contactprocess',views.contactprocess)
]