from django.urls import path
from . import views

urlpatterns = [
path('registro',  views.registro, name="registro"),
path('registro_agrupacion', views.registro_agrupacion, name="registro_agrupacion"),
path('acceso', views.acceso, name="acceso"),
path('logout', views.logout, name="logout"),
]

