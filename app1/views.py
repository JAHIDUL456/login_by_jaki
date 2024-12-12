from django.shortcuts import render

# Create your views here.

def hompage(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

