from django import forms

#importamos el modelo de persona
from .models import Persona

input_attrs = {'class' : 'form-control text-right mb-2'}

class EmailForm(forms.Form):
    email = forms.CharField(label='Correo Electrónico', max_length=30,widget=forms.TextInput(input_attrs))

class RegistroPersonaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50,widget=forms.TextInput(input_attrs))
    a_paterno = forms.CharField(label='Apellido Paterno', max_length=50,widget=forms.TextInput(input_attrs))
    a_materno = forms.CharField(label='Apellido Materno', max_length=50,widget=forms.TextInput(input_attrs))