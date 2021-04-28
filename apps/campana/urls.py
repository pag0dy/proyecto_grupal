from django.urls import path
from . import views

urlpatterns = [
	path('campana/<int:id>',  views.campana, name='campana'),
	path('agregar_campana/',  views.agregar_campana, name='agregar_campana'),
	path('agregar_aporte/<id_campana>',  views.agregar_aporte, name='agregar_aporte'),
	path('panel_control_agrupacion',  views.panel_control_agrupacion, name='panel_control_agrupacion'),
	path('panel_control_campana/<int:ids>',  views.panel_control_campana, name='panel_control_campana'),
	path('pago_aprobado', views.pago_aprobado, name='pago_aprobado'),
]