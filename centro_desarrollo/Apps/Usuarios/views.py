from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'home_rep.html')

def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect(home)
            else:
                form.add_error(None,'Revisa tus datos')
                return render(request,'login.html',{'form':form})

        else:
            return HttpResponse('Revisa tus datos')
    else:
        form = LoginForm()
        mensaje = 'mensaje desde la view App Usuarios'
        return render(request,'login.html',{'mensaje':mensaje,'form':form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']

            user, created = User.objects.get_or_create(
                username = username,
                email = email,
            )

            if created:
                form.add_error(None,'Usuario creado exitosamente')
                return render(request,'login.html',{'form':form})

            else:
                #Se regresa sin add_error pero django ya implementa el error de que el usuario existe o email
                return render(request, 'register.html',{'form':form})

        else:
            return render(request, 'register.html',{'form':form})
    else:
        form = RegisterForm()
        return render(request,'register.html',{'form':form})

