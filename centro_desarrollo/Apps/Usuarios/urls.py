from django.contrib import admin
from django.urls import path
from Apps.Usuarios import views as views_usuarios

urlpatterns = [
    path('',views_usuarios.loginn, name="login"),
    path('reproduccion',views_usuarios.home, name="home"),
    path('register',views_usuarios.register, name="register")
]
