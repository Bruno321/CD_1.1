from django.contrib import admin
from django.urls import path
from Apps.Usuarios import views as views_usuarios

urlpatterns = [
    path('home',views_usuarios.home, name="home"),
]
