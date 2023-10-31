from django.urls import path
from . import  views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout',views.loginUser, name='logout'),
    
    
]
