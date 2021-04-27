from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import FormularioCampana, FormularioAporte
from .models import Campana, Agrupacion
import bcrypt

def campana(request):
	return render(request, 'campana/dashboard_campana.html')

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
		if form.is_valid():
				nuevo_aporte = form.save(commit=False)
				nuevo_aporte.campana = Campana.objects.get(id=id_campana)
				nuevo_aporte.usuario = Usuario.objects.get(id=request.session['id'])
				nuevo_aporte.save()
				return redirect('/campana')
		else:
			context = {
				'form': form
			}
			return render(request, 'campana/registro.html', context)
	else:
		context = {
			'form' : FormularioAporte(),
		}		
		return render(request, 'campana/registro.html', context)
