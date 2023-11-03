from .models import TraderUsers
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import random


# Create your views here.

def registerUser(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "The Password and Conform Password Do not match")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "A user with this email already exists.")
            return redirect('signin')
        
        user = User.objects.create_user(firstname=firstname, lastname=lastname, username=username, email=email, password=password1)
        user.save()
        if user:
            login(request, user)
            return redirect('index',pk = user.id)
        else:
            messages.error(request, "An error occured while creating your account")
            
    return render(request, "dashboardTemplates/signup.html")

def registerAdminUser(request):
    # form = TraderUserForm()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        user.save()
        if user:
            login(request, user)
            return redirect('index',pk = user.id)
        else:
            messages.error(request, "An error occured while creating your account")
        context = {
            "user": user,
        }
    return render(request, "dashboardTemplates/signup.html", context)

def loginUser(request):
    page = 'login'
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")  
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index', pk = user.id)
        else:
            messages.error(request, "Username or Password is incorrect")
    context = {"page":page}
    return render(request, "dashboardTemplates/signin.html", context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def index(request, pk):
    print(pk, "11111111")
    user = User.objects.get(id=pk)
    if request.user.is_admin == True:
        print(user)

        return render(request, "dashboardTemplates/admin/index.html")
    elif request.user.is_admin == False:
    # user = User.objects.get(id=request.id)
        print(user)
    random_user = random.randint(-100, 100)

        
    return render(request, "dashboardTemplates/index.html")
    # else:
    #     messages.error(request, "Your are not authorised to enter the Dashboard. Please login or Sign Up")
    #     return redirect('loginUser')