from django import forms
from .models import *

class FormularioCampana(forms.ModelForm):
    class Meta:
        model = Campana
        fields = [
            'titulo',
            'descripcion',
            'fecha_limite',
            'meta',
            'imagen'
        ]
        labels = {
            'titulo': 'Titulo',
            'descripcion': 'Descripción',
            'fecha_limite': 'Fecha limite (Opcional)',
            'meta': 'Meta'
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': '40', 'rows': '10'}),
            'fecha_limite': forms.DateInput(attrs = {'type': 'date'}),
        }

class FormularioAporte(forms.ModelForm):
    class Meta:
        model = Aporte 
        fields = [
            'cantidad'
        ]
        labels = {
            'cantidad': 'Cantidad a aportar'
        }