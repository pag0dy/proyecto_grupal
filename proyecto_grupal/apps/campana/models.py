from django.db import models
from ..registro_acceso.models import *

class Campana(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    fecha_limite = models.DateTimeField()
    # pocentaje = ?
    agrupacion = models.ForeignKey(Agrupacion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recurso(models.Model):
    tipo = models.CharField(max_length=60)
    cantidad = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Aporte(models.Model):
    tipo = models.CharField(max_length=60)
    estado = models.CharField(max_length=45)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
