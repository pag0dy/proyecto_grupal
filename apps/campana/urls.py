from django.urls import path
from . import views

urlpatterns = [
	path('campana/',  views.campana, name='campana'),
]
