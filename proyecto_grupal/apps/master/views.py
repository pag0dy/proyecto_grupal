from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return HttpResponse('Creado en un abrir y cerrar de ojos')