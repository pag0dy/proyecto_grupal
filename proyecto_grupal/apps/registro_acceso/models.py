from django.db import models

class Region(models.Model):
    region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    # patrocinador = ?
    password = models.CharField(max_length=80)
    region = models.OneToOneField(Region, on_delete=models.CASCADE, primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Agrupacion(models.Model):
    nombre = models.CharField(max_length=150)
    rut = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    password = models.CharField(max_length=80)
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE, primary_key=True,)
    region = models.OneToOneField(Region, on_delete=models.CASCADE, primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
