from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)

        if user is not None:
            auth.login(request, user)
            # massage login succesfully
            return redirect('/')
        else:
            # error massage nvalid credentils
            return redirect('login')
    
    return render(request, 'accounts/login.html' )


def register(request):
    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                # massega username already taken
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # massage email aready exist
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username = username,
                    password = password, email = email
                )
                # massage account created succesuful
                return redirect('login')
        else:
            # massage password doesnt match
            return redirect('register')
    return render(request, 'accounts/register.html')

