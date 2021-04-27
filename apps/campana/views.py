from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import FormularioCampana
from .models import Campana, Agrupacion
import bcrypt

def campana(request):
	return render(request, 'campana/dashboard_campana.html')

def agregar_campana(request):
	if request.method == 'POST':
		form = FormularioCampana(request.POST)
		if form.is_valid():
				nueva_campana = form.save(commit=False)
				cdnueva_campana.agrupacion = Agrupacion.objects.get(id=request.session['idagrupacion'])
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


