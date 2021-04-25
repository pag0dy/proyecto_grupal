from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from apps.registro_acceso.forms import *
from .models import Usuario, Categoria, Agrupacion
import bcrypt

def registro(request):
	if request.method == 'POST':
		form = RegistroUsuarios(request.POST)
		if form.is_valid():
				nuevo_usuario = form.save(commit=False)
				password = form.clean_password()
				if password:
					pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
					nuevo_usuario.password = pw_hash
					nuevo_usuario.save()
					request.session['id'] = Usuario.objects.last().id
					return redirect('/dashboard')
		else:
			return redirect('registro')
	else:
		context = {
			'form' : RegistroUsuarios()
		}		
		return render(request, 'registro_acceso/registro.html', context)


def acceso(request):
	if request.method == 'POST':
		form = IngresoUsuarios(request.POST)
		if form.is_valid():
			usuario = Usuario.objects.filter(email=request.POST['email'])
			logged_user = usuario[0]
			if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
				request.session['id'] = logged_user.id
				return redirect('/dashboard')
	else:
		context = {
			'form' : IngresoUsuarios()
		}

	return render(request, 'registro_acceso/acceso.html', context)


