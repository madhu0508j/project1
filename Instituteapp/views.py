from django.shortcuts import render,redirect
from Instituteapp.models import Contact,Admission

# Create your views here.

def show(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def Course(request):
    return render(request,'Courses.html')

def admission1(request):
    return render(request,'admission.html')

def contact(request):
    return render(request,'contact.html')

def policy(request):
    return render(request,'policy.html')

def refund(request):
    return render(request,'refund.html')

def terms(request):
    return render(request,'terms.html')


def admission(request):
    if request.method=='POST':
        if request.POST.get('ADMIN')=='ADMIN':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          course=request.POST.get('course')
          message=request.POST.get('message')
          Admission.objects.create(name=name,email=email,phone=phone,course=course,message=message)
          return redirect('admission')
    
    return render(request,'admission.html')


def Contactus(request):
    if request.method=='POST':
        if request.POST.get('CONTACT')=='CONTACT':
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         message=request.POST.get('message')

         Contact.objects.create(name=name,email=email,phone=phone,message=message)

         return redirect('Contactus')
    
    return render(request,'contact.html')
    
