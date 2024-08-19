from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def sign_upfun(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Password and Conform Password are not same")
        
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login_page')
    
    
    
        # return HttpResponse('User Has been created Successfully.')
        # print(uname,email,pass1,pass2)
    
    return render(request,'sign_up.html')

def login_fun(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(request, username=username, password=pass1)
        # print(username,pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is inccorect")

    return render(request,'login_page.html')

def LogoutPage(request):
    logout(request)
    return redirect('login_page')

