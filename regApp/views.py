from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.urls import reverse


from .models import RegisterUserModel


def registerPage(request):
    return render(request,'signupForm.html')



def navigateToLoginPage(request):
    return render(request,'loginForm.html')

def signup(request):
    
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            try:
                user=User.objects.get(first_name = request.POST['phone_number'])
                messages.info(request,'Phone number Already Exists')
                return render(request,'signupForm.html')

            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'],
                                                password = request.POST['password1'],
                                                first_name = request.POST['phone_number'],
                                                email = request.POST['email'],
                                                )
                registered_user = RegisterUserModel.objects.create(
                    username=request.POST['username'],
                    phone_number=request.POST['phone_number'],
                    email=request.POST['email'],
                    
                    
                    
                )
                auth.login(request,user)
                return redirect(reverse('register'))
        else:
            messages.info(request,'password must match')
            return render(request,'signupForm.html')
    else:
        return redirect(request,'signupForm.html')


def login(request):
   
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password2']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credenitials')
            return redirect(reverse('login'))
    else:
        return render(request,'loginForm.html')
def logout(request):
    auth.logout(request)
    return redirect("/")