from django.shortcuts import render, redirect, HttpResponse

def registro(request):
	return render(request, 'registro_acceso/registro.html')

def acceso(request):
	return render(request, 'registro_acceso/acceso.html')