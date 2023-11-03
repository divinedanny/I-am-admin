from django.urls import path
from . import  views

# app_name = "tradeUser"
# 
urlpatterns = [
    path('home/<uuid:pk', views.index, name='index'),
    path('', views.registerUser, name='register'),
    path('login/', views.loginUser, name='signin'),
    path('logout',views.loginUser, name='signout'),
    
    
]
