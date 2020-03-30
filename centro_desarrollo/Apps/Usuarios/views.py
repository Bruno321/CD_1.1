from django.shortcuts import render, HttpResponse

# Create your views here.
def renderizado(request):
    return HttpResponse('mensaje por httpresponsejasjd')

def home(request):
    mensaje = 'mensaje desde la view App Usuarios'
    return render(request,'reproduccion_home.html',{'mensaje':mensaje})