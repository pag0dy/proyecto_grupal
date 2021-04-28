from django.shortcuts import render, redirect, HttpResponse
from ..registro_acceso.models import Agrupacion, Usuario

def filtro_usuario(id_usuario):
    activo = Usuario.objects.filter(id = id_usuario)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
    else:
        mensaje = 'No se encontró el usuario'
        print(mensaje)
        return mensaje

def filtro_agrupacion(id_agrupacion):
    activo = Agrupacion.objects.filter(id = id_agrupacion)
    if activo:
        agrupacion_activa = activo[0]
        return agrupacion_activa
    else:
        mensaje = 'No se encontró la agrupacion'
        print(mensaje)
        return mensaje

def index(request):
	return render(request, 'master/bienvenida.html')

def dashboard(request):
	agrup = filtro_agrupacion(request.session['idagrupacion'])
	usuario = filtro_usuario(request.session['id'])
	agrupaciones = Agrupacion.objects.all().order_by('-created_at')[:3]
	print(agrupaciones)
	context = {
		'agrupaciones': agrupaciones,
		'usuario': usuario
	}
	return render(request, 'master/explorar.html', context)

def perfil(request, id):
	agrupacion = filtro_agrupacion(id)
	usuario = filtro_usuario(request.session['id'])
	agrup = filtro_agrupacion(request.session['idagrupacion'])
	context = {
		'agrup':agrup,
		'usuario':usuario,
		'agrupacion':agrupacion
	}
	return render(request, 'master/perfil.html', context)