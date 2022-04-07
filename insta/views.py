from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
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
    return render(request,'login.html')
