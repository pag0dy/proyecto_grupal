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
	agrupaciones = Agrupacion.objects.all().order_by('-created_at')[:3]
	if 'idagrupacion' in request.session:
		agrup = filtro_agrupacion(request.session['idagrupacion'])
		context = {
			'agrupaciones': agrupaciones,
			'agrup': agrup
		}
	elif 'id' in request.session:
		usuario = filtro_usuario(request.session['id'])
		context = {
			'agrupaciones': agrupaciones,
			'usuario': usuario
		}
	else:
		context = {
			'agrupaciones':agrupaciones
		}
	return render(request, 'master/explorar.html', context)

def perfil(request, id):
	agrupacion = filtro_agrupacion(id)
	campanas = agrupacion.campana_activa.all()
	if 'idagrupacion' in request.session:
		agrup = filtro_agrupacion(request.session['idagrupacion'])
		context = {
			'agrup':agrup,
			'agrupacion':agrupacion,
			'campanas': campanas
		}	
	elif 'id' in request.session:
		usuario = filtro_usuario(request.session['id'])
		context = {
			'usuario':usuario,
			'agrupacion':agrupacion,
			'campanas': campanas
		}
	else: 
		context = {
			'agrupacion':agrupacion,
			'campanas': campanas
		}
	return render(request, 'master/perfil.html', context)