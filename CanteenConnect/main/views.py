from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth, messages
from django.contrib.auth.decorators import user_passes_test
from .models import Menu


#Testing
def chef_check(user):
    '''To check if user is chef'''
    return user.groups.filter(name='chef').exists()
def student_check(user):
    '''To check if user is student'''
    return user.groups.filter(name='student').exists()



#Functions 
def login(request):
    '''allows user to log into site is & capable of diffrentiating between chef and student'''
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if user.groups.filter(name='chef').exists():
                return redirect('home_c')
            return redirect('home_s')
        else:
            messages.error(request,'Username or Password Incorrect.')
            return render (request,'login.html')#Redirects if error is present
    else:
        return render(request,'login.html')#Not sure what this is for

def logout(request):
    auth.logout(request)
    return redirect('login')



#Site Rendering Functions
@user_passes_test(student_check)#to only allow if user is student
def student_home(request):
    return render(request,'student_home.html',{})

@user_passes_test(chef_check)#to only allow if user is chef
def chef_home(request):
    return render(request,'chef_home.html',{})

@user_passes_test(chef_check)
def chef_select(request):
    return render(request,'chef_inserter.html',{})