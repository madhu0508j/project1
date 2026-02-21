from django.shortcuts import render

# Create your views here.

def show(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def Course(request):
    return render(request,'Courses.html')

def admission(request):
    return render(request,'admission.html')

def contact(request):
    return render(request,'contact.html')

def policy(request):
    return render(request,'policy.html')

def refund(request):
    return render(request,'refund.html')

def terms(request):
    return render(request,'terms.html')