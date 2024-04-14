from django.urls import path
from . import views
# from .views import index, accion, deportes, disparos, estrategia, formulario, rol
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('accion', views.accion, name='accion'),
    path('deportes', views.deportes, name='deportes'),
    path('disparos', views.disparos, name='disparos'),
    path('estrategia', views.estrategia, name='estrategia'),
    path('rol', views.Rol, name='rol'),
    path('formulario', views.formulario, name='formulario'),
    
]