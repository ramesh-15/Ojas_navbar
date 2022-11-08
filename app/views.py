from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def python(request):
    return render(request,'python.html')

def java(request):
    return render(request,'java.html')

def devops(request):
    return render(request,'devops.html')