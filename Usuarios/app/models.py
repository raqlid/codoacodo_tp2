# users/models.py
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombres")
    apellido = models.CharField(max_length=50, verbose_name="Apellidos")
    usuario = models.CharField(max_length=50, verbose_name="Usuario")
    email = models.CharField(max_length=50, verbose_name="Email")
    dni = models.CharField(max_length=10, unique=True, verbose_name="DNI")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    fecha_baja = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de baja")
    password = models.CharField(max_length=50, verbose_name="Contraseña")

