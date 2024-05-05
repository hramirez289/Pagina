from django.urls import path
from . import views
from django.conf import Settings
from django.conf.urls.static import static
# from .views import UsuarioView

urlpatterns = [
    path('', views.index, name='index'),
    path('accion', views.accion, name='accion'),
    path('deportes', views.deportes, name='deportes'),
    path('disparos', views.disparos, name='disparos'),
    path('estrategia', views.estrategia, name='estrategia'),
    path('rol',views.Rol, name='rol'),
    path('formulario', views.formulario, name='formulario'),
    path('crearUsuario', views.crearUsuario)
    
]


# from django.urls import path, include
# from rest_framework import routers
# from myapp import views

# router=routers.DefaultRouter()
# router.register("", views.UsuarioView)
