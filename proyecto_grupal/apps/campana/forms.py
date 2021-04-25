from django import forms
from .models import *

class FormularioCampana(forms.ModelForm):
    class Meta:
        model = Campana
        fields = [
            'titulo',
            'descripcion',
            'fecha_limite',
            'agrupacion',
            'meta'
        ]
        labels = {
            'titulo': 'Titulo',
            'descripcion': 'Descripción',
            'fecha_limite': 'Fecha limite (Opcional)',
            'agrupacion': 'Agrupación',
            'meta': 'Meta'
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': '40', 'rows': '10'})
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 4:
            raise forms.ValidationError(
                'El titulo de la campaña debe constar al menos de 3 caracteres.'
                )
            return titulo
        
    def clean_descripcion(self):
        descripcion = self.cleanded_data.get('descripcion')
        if len(descripcion) < 50:
            raise forms.ValidationError(
                'Por favor, detalla los aspectos generales de tu campaña.'
                )
            return descripcion

