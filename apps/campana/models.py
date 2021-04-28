from django.db import models
from ..registro_acceso.models import *

class Campana(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=750)
    fecha_limite = models.DateTimeField(blank=True, null=True)
    agrupacion = models.ManyToManyField(Agrupacion, related_name='campana_activa')
    recaudacion = models.PositiveIntegerField(default=0)
    meta = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Aporte(models.Model):
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE, related_name='aporte_ingresado')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='aporte_usuario')
    cantidad = models.PositiveIntegerField(default=0)
    aprobado = models.BooleanField(default=False)
    rechazado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
