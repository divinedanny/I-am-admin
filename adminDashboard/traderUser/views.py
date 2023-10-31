from .models import TraderUser
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import TraderUserForm
import random


# Create your views here.

def registerUser(request):
    form = TraderUserForm()
    if request.method == "POST":
        form = TraderUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "An error occured while creating your account")
            
    context = {"form":form}
    return render(request, "dashboardTemplates/signup.html", context)

def registerAdminUser(request):
    form = TraderUserForm()
    if request.method == "POST":
        form = TraderUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "An error occured while creating your account")
            
    context = {"form":form}
    return render(request, "templates/dashboardTemplates/signup.html", context)

def loginUser(request):
    page = 'login'
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = TraderUser.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")  
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Username or Password is incorrect")
    context = {"page":page}
    return render(request, "dashboardTemplates/signin.html", context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def index(request):

    if request.user.is_admin == True:
 
        return render(request, "dashboardTemplates/admin/index.html")
    elif request.user.is_admin == False:
        random_user = random.randint(-100, 100)

        
        return render(request, "dashboardTemplates/index.html")