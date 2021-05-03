from django.urls import path
from . import views

urlpatterns = [
path('registro',  views.registro, name="registro"),
path('registro_agrupacion', views.registro_agrupacion, name="registro_agrupacion"),
path('acceso', views.acceso, name="acceso"),
path('acceso_agrupacion', views.acceso_agrupacion, name="acceso_agrupacion"),
path('editar_agrupacion', views.editar_agrupacion, name="editar_agrupacion"),
path('logout', views.logout, name="logout"),
]

