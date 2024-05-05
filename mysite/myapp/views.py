# from rest_framework import viewsets
# from .serializers import UsuarioSerializer
# from .models import Usuario

# class UsuarioView(viewsets.ModelViewSet):
#     queryset=Usuario.objects.all()
#     serializer_class=UsuarioSerializer






from django.shortcuts import redirect, render
from django.conf.urls.static import static
from .models import Usuario
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

def crearUsuario(request):
    nombre_completo = request.POST["nombre"]
    nombre_usuario = request.POST["usuario"]
    correo_electronico = request.POST["mail"]
    clave_acceso = request.POST["clave"]
    fecha_nacimiento = request.POST["fechanac"]
    direccion_despacho = request.POST["dirdesp"]

    usuario=Usuario.objects.create(nombre_completo=nombre_completo, nombre_usuario=nombre_usuario,correo_electronico=correo_electronico, clave_acceso=clave_acceso, fecha_nacimiento=fecha_nacimiento,direccion_despacho=direccion_despacho)
    return redirect("/")

