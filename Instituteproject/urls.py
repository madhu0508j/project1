"""
URL configuration for Instituteproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Instituteapp.views import show,about,Course,admission1,contact,policy,refund,terms,Contactus,admission


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',show,name='index'),
    path('about/',about,name='about'),
    path('courses/',Course,name='courses'),
    path('admission/',admission1,name='admissionn'),
    path('contact/',contact,name='contact'),
    path('Term&Policy/',policy,name='policy'),
    path('refund/',refund,name='refund'),
    path('terms/',terms,name='terms'),
    path('Admission/',admission,name='admission'),
    path('Contact/',Contactus,name='Contactus')
]
