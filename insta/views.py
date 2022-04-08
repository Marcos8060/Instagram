from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password'] 

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists!')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            print('user created')
            return redirect('login')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')


