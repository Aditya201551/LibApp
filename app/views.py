from django.shortcuts import render
from app.forms import userForm
# Create your views here.

#login modules

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"app/index.html")

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, "app/login.html")

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login but failed:")
            print(f"Username: {username}\nPassword: {password}")
            return HttpResponse("</h1> INVALID LOGIN DETAILS: LOGIN AGAIN </h1>")
    else:
        return render(request, "app/login.html")

@login_required()
def user_logout(request):
    logout(request)
    return render(request, "app/index.html")

def register(request):
    registered=False

    if request.method=="POST":
        user_form=userForm(data=request.POST)

        if user_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=userForm()
    return render(request, "app/register.html", context={"user_form":user_form, "registered":registered})

def preference(request):    
    return render(request, "app/preference.html")

def dashboard(request):
    return render(request, "app/dashboard.html")


def sites(request):
    return render(request, 'app/sites.html')
