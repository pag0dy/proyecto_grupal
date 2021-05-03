from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import RegistroAgrupaciones, RegistroUsuarios, IngresoAgrupaciones, IngresoUsuarios, EditarAgrupacion
from .models import Usuario, Categoria, Agrupacion
from ..campana.forms import FormularioCampana
import bcrypt


def filtro_usuario(id_usuario):
    activo = Usuario.objects.filter(id=id_usuario)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
    else:
        mensaje = 'No se encontró el usuario'
        print(mensaje)
        return mensaje


def filtro_agrupacion(id_agrupacion):
    activo = Agrupacion.objects.filter(id=id_agrupacion)
    if activo:
        agrupacion_activa = activo[0]
        return agrupacion_activa
    else:
        mensaje = 'No se encontró la agrupacion'
        print(mensaje)
        return mensaje


def registro(request):
	if request.method == 'POST':
		form = RegistroUsuarios(request.POST)
		if form.is_valid():
				nuevo_usuario = form.save(commit=False)
				pw_hash = bcrypt.hashpw(
				    request.POST['password'].encode(), bcrypt.gensalt()).decode()
				nuevo_usuario.password = pw_hash
				nuevo_usuario.save()
				request.session['id'] = Usuario.objects.last().id
				return redirect('/dashboard')
		else:
			context = {
				'form': form,
			}
			return render(request, 'registro_acceso/registro.html', context)
	else:
		context = {
			'form': RegistroUsuarios(),
		}
		return render(request, 'registro_acceso/registro.html', context)


def registro_agrupacion(request):
	if request.method == 'POST':
		form = RegistroAgrupaciones(request.POST)
		print(request.POST)
		if form.is_valid():
			nueva_agrupacion = form.save(commit=False)
			pw_hash = bcrypt.hashpw(
				request.POST['password'].encode(), bcrypt.gensalt()).decode()
			nueva_agrupacion.password = pw_hash
			nueva_agrupacion.save()
			request.session['idagrupacion'] = Agrupacion.objects.last().id
			print(request.session['idagrupacion'])
			return redirect('/dashboard')
		else:
			context = {
				'group_form': form,

			}
			return render(request, 'registro_acceso/registro_agrupacion.html', context)
	else:
			context = {
				'group_form': RegistroAgrupaciones(),
			}
			return render(request, 'registro_acceso/registro_agrupacion.html', context)


def acceso(request):
	if request.method == 'POST':
		print(request.POST)
		form = IngresoUsuarios(request.POST)
		if form.is_valid():
			usuario = Usuario.objects.filter(email=request.POST['email'])
			logged_user = usuario[0]
			if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
				request.session['id'] = logged_user.id
				return redirect('/dashboard')
		else:
			context = {
				'form': form,
			}

			return render(request, 'registro_acceso/acceso.html', context)

	else:
		context = {
			'form': IngresoUsuarios(),
		}

		return render(request, 'registro_acceso/acceso.html', context)


def acceso_agrupacion(request):
	if request.method == 'POST':
		form = IngresoAgrupaciones(request.POST)
		print(form.is_valid())
		if form.is_valid():
			logged_agrupacion = Agrupacion.objects.get(email = request.POST['email'])
			request.session['idagrupacion'] = logged_agrupacion.id
			return redirect('/dashboard')
		else:
			context = {
				'group_form': form,
			}

			return render(request, 'registro_acceso/acceso_agrupacion.html', context)

	else:
		context = {
			'group_form': IngresoAgrupaciones(),
		}

		return render(request, 'registro_acceso/acceso_agrupacion.html', context)


def logout(request):
    logged_user=[]
    request.session.clear()
    return redirect("/")

def editar_agrupacion(request):
	if request.method == 'POST':
		form = EditarAgrupacion()
		print(form.is_valid())
		if form.is_valid():
			agrupacion = filtro_agrupacion(request.POST['id_agrupacion'])
			agrupacion.nombre = request.POST['nombre']
			print(agrupacion.nombre)
			agrupacion.rut = request.POST['rut']
			print(agrupacion.rut)
			agrupacion.email = request.POST['email']
			print(agrupacion.email)
			agrupacion.descripcion = request.POST['descripcion']
			print(agrupacion.descripcion)
			agrupacion.categoria = request.POST['categoria']
			print(agrupacion.categoria)
			agrupacion.necesitamos = request.POST['necesitamos']
			print(agrupacion.necesitamos)
			agrupacion.contacto = request.POST['contacto']
			print(agrupacion.contacto)
			agrupacion.save()
			return redirect('campana/panel_control.html')
		else:
			context = {
				'form':form,
				'campana_form':FormularioCampana()
			}
			return render(request, 'campana/panel-control.html', context)