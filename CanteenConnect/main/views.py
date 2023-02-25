from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if user.groups.filter(name='chef').exists():
                return redirect('home_c')
            return redirect('home_s')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

@login_required
def student_home(request):
    return render(request,'student_home.html',{})

@login_required
def chef_home(request):
    return render(request,'chef_home.html',{})
