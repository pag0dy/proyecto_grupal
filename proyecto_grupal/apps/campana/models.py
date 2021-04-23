from django.db import models
from ..registro_acceso.models import *

class Campana(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=750)
    fecha_limite = models.DateTimeField()
    agrupacion = models.ForeignKey(Agrupacion, on_delete=models.CASCADE)
    # Falta incorporar un campo de porcentaje de cumplimiento de la meta de la campaña 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recurso(models.Model):
    tipo = models.CharField(max_length=60) # Incorporar: choices
    cantidad = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Aporte(models.Model):
    tipo = models.CharField(max_length=60)
    estado = models.CharField(max_length=45) # Este campo de estado no sería lo mismo que el campo aprobado? 
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    aprobado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
