from django.shortcuts import render, redirect, HttpResponse
from apps.registro_acceso.forms import *

def prueba(request):
	return HttpResponse('para pruebas de formularios')