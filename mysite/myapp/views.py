from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.

def index(request):
    return render(request, 'index.html')

def accion(request):
    return render(request, 'accion.html')

def deportes(request):
    return render(request, 'deportes.html')

def disparos(request):
    return render(request, 'disparos.html')

def estrategia(request):
    return render(request, 'estrategia.html')

def Rol(request):
    return render(request, 'Rol.html')

def formulario(request):
    return render(request, 'formulario.html')