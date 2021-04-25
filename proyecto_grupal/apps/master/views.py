from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, 'master/bienvenida.html')

def dashboard(request):
	return render(request, 'master/explorar.html')

def perfil(request):
	return render(request, 'master/perfil.html')