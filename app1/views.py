from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def hompage(request):
    return render(request,'home.html')


def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            return HttpResponse('wrong credentials')
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        psw1=request.POST.get('password1')
        email=request.POST.get('email')
        psw2=request.POST.get('password2')
        if psw1==psw2:
            my_user=User.objects.create_user(uname,email,psw1)
            my_user.save()
            return redirect('login')
        else:
            return HttpResponse('sir your confirm password is different')
            
    return render(request,'signup.html')

