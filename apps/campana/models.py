from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, validate_slug, EmailValidator
from ..registro_acceso.models import *

class Campana(models.Model):
    titulo = models.CharField(max_length=100, validators = [MinLengthValidator(limit_value = 2, message = 'El título debe tener más de dos caracteres')])
    descripcion = models.TextField(max_length=750, validators = [MinLengthValidator(limit_value = 50, message = 'Ingresa una descripción de al menos 50 caracteres de la campaña')])
    fecha_limite = models.DateTimeField(blank=True, null=True)
    agrupacion = models.ManyToManyField(Agrupacion, related_name='campana_activa')
    recaudacion = models.PositiveIntegerField(default=0)
    meta = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='images/', blank=True)
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
