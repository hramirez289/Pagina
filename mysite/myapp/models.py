from django.db import models

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    clave_acceso = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    direccion_despacho = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre_usuario