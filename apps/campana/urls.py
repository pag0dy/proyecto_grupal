from django.urls import path
from . import views

urlpatterns = [
	path('campana/',  views.campana, name='campana'),
	path('agregar_campana/',  views.agregar_campana, name='agregar_campana'),
]
