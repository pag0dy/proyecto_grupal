from .models import Agrupacion, Usuario
from django import forms
import bcrypt
import re

# Formulario de registro usuarios


class RegistroUsuarios(forms.ModelForm):
    password_confirm = forms.CharField(
        max_length=255, label='Confirm Password')
    password_confirm.widget = forms.TextInput(attrs={'type': 'password'})

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'rut', 'email', 'password',]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
        }
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'}),
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'rut': forms.TextInput(),
            'email': forms.TextInput(),
        }

# Validaciones registro usuarios

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not valid_names(nombre):
            raise forms.ValidationError('Ingresa un nombre válido.')
        if len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not valid_names(apellido):
            raise forms.ValidationError(
                'Ingresa un apellido válido'
            )
        if len(apellido) < 3:
            raise forms.ValidationError(
                'El apellido debe tener al menos 3 caracteres.'
            )
        return apellido

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not valid_rut(rut):  # Regex para formato 12345678-9
            raise forms.ValidationError(
                'Ingresa un RUT válido.'
            )
        if len(rut) < 10:
            raise forms.ValidationError(
                'El rut debe tener 10 caracteres incluyendo el guión.'
            )
        return rut

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = Usuario.objects.filter(email=email)
        if not valid_email(email):
            raise forms.ValidationError(
                'Ingresa un correo válido.'
            )
        if user:
            raise forms.ValidationError(
                'El correo ya está en uso.'
            )
        if len(email) < 10:
            raise forms.ValidationError(
                'El correo debe tener al menos 10 caracteres.'
            )
        return email

    def clean(self):
        cleaned_data = super(RegistroUsuarios, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError(
                {
                    'password': 'Las contraseñas no coinciden.'
                }
            )
        if len(password) < 8:
            raise forms.ValidationError(
                {
                    'password': 'La contraseña debe tener al menos 8 caracteres.'
                }
            )
        if len(password_confirm) < 10:
            raise forms.ValidationError(
                {
                    'password': 'La contraseña debe tener al menos 8 caracteres.'
                }
            )


# Formulario de ingreso usuarios

class IngresoUsuarios(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'email',
            'password',
        ]
        widgets = {
            'email': forms.TextInput(),
            'password': forms.TextInput(attrs={'type': 'password'})
        }


# validaciones formulario ingreso usuario

    def clean(self):
        cleaned_data = super(IngresoUsuarios, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = Usuario.objects.filter(email=email)
        if not user:
            raise forms.ValidationError(
                {
                    'email': 'Correo no registrado.'
                }
            )
        if len(email) < 10:
            raise forms.ValidationError(
                {
                    'email': 'El email debe tener al menos 10 caracteres.'
                }
            )
        user = user[0]
        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            raise forms.ValidationError(
                {
                    'password': 'Contraseña equivocada.'
                }
            )
        return cleaned_data


# Formulario de registro agrupaciones

class RegistroAgrupaciones(forms.ModelForm):
    password_confirm = forms.CharField(
        max_length=255, label='Confirm Password')
    password_confirm.widget = forms.TextInput(attrs={'type': 'password'})

    class Meta:
        model = Agrupacion
        fields = [
            'nombre',
            'rut',
            'email',
            'categoria',
            'descripcion',
            'group_password',
            'necesitamos',
            'contacto'
        ]
        labels = {
            'nombre': 'Nombre',
            'rut': 'RUT',
            'email': 'Correo electrónico',
            'categoria': 'Categoría',
            'descripcion': 'Descripción',
            'group_password': 'Contraseña',
            'necesitamos': 'Necesitamos',
            'contacto': 'Contacto'
        }
        widgets = {
            'group_password': forms.TextInput(attrs={'type': 'password'}),
            'descripcion': forms.TextInput(attrs={'cols':5,'rows':10}),
            'necesitamos': forms.TextInput(attrs={'cols':5,'rows':10})
        }


# Validaciones registro agrupaciones

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not valid_names(nombre):
            raise forms.ValidationError('Ingresa un nombre válido.')
        if len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )
        return nombre

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not valid_rut(rut):  # Regex para formato 12345678-9
            raise forms.ValidationError(
                'Ingresa un RUT válido.'
            )
        if len(rut) < 10:
            raise forms.ValidationError(
                'El rut debe tener 10 caracteres incluyendo el guión.'
            )
        return rut

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = Agrupacion.objects.filter(email=email)
        if not valid_email(email):
            raise forms.ValidationError(
                'Ingresa un correo válido.'
            )
        if user:
            raise forms.ValidationError(
                'El correo ya está en uso.'
            )
        if len(email) < 10:
            raise forms.ValidationError(
                'El correo debe tener al menos 10 caracteres.'
            )
        return email

    def clean(self):
        cleaned_data = super(RegistroAgrupaciones, self).clean()
        password = cleaned_data.get('group_password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError(
                {
                    'password': 'Las contraseñas no coinciden.'
                }
            )
        if len(password) < 8:
            raise forms.ValidationError(
                {
                    'group_password': 'La contraseña debe tener al menos 8 caracteres.'
                }
            )



# Formulario de ingreso agrupaciones

class IngresoAgrupaciones(forms.ModelForm):
    class Meta:
        model = Agrupacion
        fields = [
            'email',
            'group_password',
        ]
        label = {
            'group_password':'Contraseña'
        }
        widgets = {
            'group_password': forms.TextInput(attrs={'type': 'password'})
        }


# validaciones formulario ingreso usuario

    def clean(self):
        cleaned_data = super(IngresoAgrupaciones, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('group_password')
        user = Agrupacion.objects.filter(email=email)
        if not user:
            raise forms.ValidationError(
                {
                    'email': 'Correo no registrado.'
                }
            )
        if len(email) < 10:
            raise forms.ValidationError(
                {
                    'email': 'El email debe tener al menos 10 caracteres.'
                }
            )
        user = user[0]
        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            raise forms.ValidationError(
                {
                    'password': 'Contraseña equivocada.'
                }
            )
        return cleaned_data


# Funciones REGEX

def valid_rut(rut):
    REGEX_RUT = re.compile(r'^(\d){7,8}-(\d|k|K)$')
    return REGEX_RUT.match(rut)


def valid_names(name):
    REGEX_NAME = re.compile(r'^[A-Za-z]+$')
    return REGEX_NAME.match(name)


def valid_email(email):
    REGEX_EMAIL = re.compile(
        r'^[a-zA-Z0-9\._-]+@[a-zA-Z0-9\.]+\.[a-zA-Z]{2,3}$'
    )
    return REGEX_EMAIL.match(email)

# Formulario edicion agrupaciones

class RegistroAgrupacionesEdit(forms.ModelForm):

    class Meta:
        model = Agrupacion
        fields = [
            'nombre',
            'email',
            'descripcion',
            'necesitamos',
        ]
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo electrónico',
            'descripcion': 'Descripción',
            'necesitamos': 'Necesitamos',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'cols':5,'rows':10}),
            'necesitamos': forms.TextInput(attrs={'cols':5,'rows':10})
        }


# Validaciones registro agrupaciones

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not valid_names(nombre):
            raise forms.ValidationError('Ingresa un nombre válido.')
        if len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )
        return nombre


    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = Agrupacion.objects.filter(email=email)
        if not valid_email(email):
            raise forms.ValidationError(
                'Ingresa un correo válido.'
            )
        if user:
            raise forms.ValidationError(
                'El correo ya está en uso.'
            )
        if len(email) < 10:
            raise forms.ValidationError(
                'El correo debe tener al menos 10 caracteres.'
            )
        return email
