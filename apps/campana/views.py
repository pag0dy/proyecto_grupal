from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import FormularioCampana, FormularioAporte
from .models import Campana, Agrupacion, Aporte
from ..registro_acceso.models import Agrupacion, Usuario
import bcrypt
from apps.registro_acceso.forms import RegistroAgrupaciones

def filtro_campana(id_campana):
    activa = Campana.objects.filter(id=id_campana)
    if activa:
        campana_activa = activa[0]
        return campana_activa
    else:
        mensaje = 'No se encontró la campana'
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

def filtro_usuario(id_usuario):
    activo = Usuario.objects.filter(id=id_usuario)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
    else:
        mensaje = 'No se encontró el usuario'
        print(mensaje)
        return mensaje

def campana(request, id):
	campana = filtro_campana(id)
	porcentaje_recaudacion = campana.recaudacion / campana.meta
	print(porcentaje_recaudacion)
	agrup = campana.agrupacion.all()
	if 'id' in request.session:
		usuario = filtro_usuario(request.session['id'])
		context = {
			'campana':campana,
			'porcentaje':porcentaje_recaudacion,
			'usuario':usuario,
			'agrup':agrup,
			'form' : FormularioAporte(),
		}
	elif 'idagrupacion' in request.session:
		agrupacion = filtro_agrupacion(request.session['idagrupacion'])
		context = {
					'campana':campana,
					'porcentaje':porcentaje_recaudacion,
					'agrupacion':agrupacion,
					'agrup':agrup,
					'form' : FormularioAporte(),
				}
	else: 
		context = {
					'campana':campana,
					'porcentaje':porcentaje_recaudacion,
					'agrup':agrup,
					'form' : FormularioAporte(),			
		}
	return render(request, 'campana/dashboard_campana.html', context)

def agregar_campana(request):
	if request.method == 'POST':
		form = FormularioCampana(request.POST)
		if form.is_valid():
				nueva_campana = form.save(commit=False)
				nueva_campana.agrupacion = Agrupacion.objects.get(id=request.session['idagrupacion'])
				nueva_campana.save()
				return redirect('/campana')
		else:
			context = {
				'form': form
			}
			return render(request, 'campana/registro.html', context)
	else:
		context = {
			'form' : FormularioCampana(),
		}		
		return render(request, 'campana/registro.html', context)

def agregar_aporte(request, id_campana):
	if request.method == 'POST':
		form = FormularioAporte(request.POST)
		campana = filtro_campana(id_campana)
		if form.is_valid():
				nuevo_aporte = form.save(commit=False)
				nuevo_aporte.campana = campana
				nuevo_aporte.usuario = Usuario.objects.get(id=request.session['id'])
				nuevo_aporte.save()
				return redirect('/campana/' + id_campana )
		else:
			return redirect('/campana/' + id_campana )
	else:
		return render(request, 'campana/registro.html', context)


def panel_control_agrupacion(request):
	agrupacion = Agrupacion.objects.get(id=request.session['idagrupacion'])
	form = RegistroAgrupaciones(instance=agrupacion)
	diff = {}
	for meta in agrupacion.campana_activa.all():
		difference = meta.meta - meta.recaudacion
		pairs = {meta.titulo : difference}
		diff.update(pairs)
	context = {
		'agrupacion': agrupacion,
		'form': form,
		'diff': diff
	}
	return render(request, 'campana/panel-control.html', context )

def panel_control_campana(request, ids):
	campana = Campana.objects.get(id=ids)
	context = { 
		'campana': campana
	}
	return render(request, 'campana/panel-control-campana.html', context)

def pago_aprobado(request):
	campana = Campana.objects.get(id = request.POST['campana_id'])
	aporte = Aporte.objects.get(id = request.POST['aporte_id'])
	recaudacion_actual = campana.recaudacion
	campana.recaudacion = recaudacion_actual + aporte.cantidad
	campana.save()
	aporte.aprobado = True
	aporte.save()
	return redirect('/panel_control_campana/' + str(campana.id))
