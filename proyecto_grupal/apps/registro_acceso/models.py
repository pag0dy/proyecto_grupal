from django.db import models

# class Region(models.Model):
# nombre = models.CharField(max_length=100)
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=80)
    # region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=750)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Agrupacion(models.Model):
    choices = [('categoria1', 'Categoría1'), ('categoria2',
                                              'Categoría2'), ('categoria3', 'Categoría3')]
    nombre = models.CharField(max_length=150)
    rut = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    descripcion = models.TextField(max_length=750)
    password = models.CharField(max_length=80)
    categoria = models.CharField(max_length=80, choices=choices)
    # region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
