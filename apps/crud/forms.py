from django import forms

#importamos el modelo de persona
from .models import Persona

class EmailForm(forms.Form):
    email = forms.CharField(label='Correo Electrónico', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control' }))

class RegistroPersonaForm(forms.Form):
    model = Persona
    widgets = {
        'nombre' :  forms.TextInput(attrs={'class' : 'form-control'})
    }