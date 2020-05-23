from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'log/index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Registered")
                return render(request, 'log/register.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Email Already Taken")
                return render(request, 'log/register.html')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password= password)
                user.save()
                messages.info(request, "Registered Successfully")
                return redirect('/log/')
        else:
            messages.info(request, "password didn't match...")
            return render(request, 'log/register.html')
    else:
        return render(request, 'log/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/log/')
        else:
            messages.info(request, 'invalid user')
            return render(request, 'log/login.html')

    else:
        return render(request, 'log/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/log/')

def checks1(request):
    return render(request, 'log/checkingpage.html')
