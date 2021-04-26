from django.shortcuts import render, redirect, HttpResponse

def campana(request):
	return render(request, 'campana/dashboard_campana.html')