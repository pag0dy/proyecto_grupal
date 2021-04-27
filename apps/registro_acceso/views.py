from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import RegistroAgrupaciones, RegistroUsuarios, IngresoAgrupaciones, IngresoUsuarios
from .models import Usuario, Categoria, Agrupacion
import bcrypt

def registro(request):
	if request.method == 'POST':
		form = RegistroUsuarios(request.POST)
		if form.is_valid():
				nuevo_usuario = form.save(commit=False)
				pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
				nuevo_usuario.password = pw_hash
				nuevo_usuario.save()
				request.session['id'] = Usuario.objects.last().id
				return redirect('/dashboard')
		else:
			context = {
				'form': form
			}
			return render(request, 'registro_acceso/registro.html', context)
	else:
		context = {
			'form' : RegistroUsuarios(),
			'group_form': RegistroAgrupaciones(),
		}		
		return render(request, 'registro_acceso/registro.html', context)

def registro_agrupacion(request, methods=['POST']):
	form = RegistroAgrupaciones(request.POST)
	if form.is_valid():
			nueva_agrupacion = form.save(commit=False)
			pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
			nueva_agrupacion.password = pw_hash
			nueva_agrupacion.save()
			request.session['idagrupacion'] = Agrupacion.objects.last().id
			return redirect('/dashboard')
	else:
		form = RegistroAgrupaciones()
		context = {
			'group_form': form
		}
		return render(request, 'registro_acceso/registro.html', context)

# def registro_agrupacion(request):
# 	if request.method == 'POST':
# 		form = RegistroAgrupaciones(request.POST)
# 		if form.is_valid():
# 			nueva_agrupacion = form.save(commit=False)
#  			pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
# 			nueva_agrupacion.password = pw_hash


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
				'form' : form
			}

			return render(request, 'registro_acceso/acceso.html', context)
		
	else:
		context = {
			'form' : IngresoUsuarios()
		}

		return render(request, 'registro_acceso/acceso.html', context)

def acceso_agrupacion(request):
	if request.method == 'POST':
		form = IngresoAgrupaciones(request.POST)
		if form.is_valid():
			agrupacion = Agrupacion.objects.filter(email=request.POST['email'])
			logged_agrupacion = agrupacion[0]
			if bcrypt.checkpw(request.POST['password'].encode(), logged_agrupacion.password.encode()):
				request.session['idagrupacion'] = logged_agrupacion.id
				return redirect('/dashboard')
		else:
			context = {
				'form' : form
			}

			return render(request, 'registro_acceso/acceso.html', context)
		
	else:
		context = {
			'form' : IngresoAgrupaciones()
		}

		return render(request, 'registro_acceso/acceso.html', context)

def logout(request):
    logged_user = []
    request.session.clear()
    return redirect("/")


