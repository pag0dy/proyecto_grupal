from django.urls import path
from . import views

urlpatterns = [
	path('',  views.index, name='index'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('perfil/<int:id>', views.perfil, name='perfil'),
	path('categorias/<str:categoria>', views.categorias, name='categorias')
]