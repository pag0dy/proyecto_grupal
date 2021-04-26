from django.urls import path
from . import views

urlpatterns = [
path('registro',  views.registro),
path('acceso', views.acceso),
path('logout', views.logout),
]

