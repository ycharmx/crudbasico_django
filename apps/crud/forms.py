from django import forms

#importamos el modelo de persona
from .models import Empleado
from django.core.validators import RegexValidator
from bootstrap_datepicker_plus import DatePickerInput

input_attrs = {'class' : 'form-control text-left mb-2'}

class EmailForm(forms.Form):
    email = forms.CharField(
            label='Correo Electrónico', max_length=30,widget=forms.TextInput(input_attrs),
            validators=[
                RegexValidator(
                    regex="^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",

                )
            ]
        )

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(
            label='Nombre', max_length=50,widget=forms.TextInput(input_attrs),
            validators = [
                RegexValidator(
                    regex = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$",
                    message = "Sólo letras"
                )
            ]            
        )
    a_paterno = forms.CharField(
            label='Apellido Paterno', max_length=50,widget=forms.TextInput(input_attrs),
             validators = [
                RegexValidator(
                    regex = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$",
                    message = "Sólo letras"
                )
            ]
        )
    a_materno = forms.CharField(
            label='Apellido Materno', max_length=50,widget=forms.TextInput(input_attrs),
             validators = [
                RegexValidator(
                    regex = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$",
                    message = "Sólo letras"
                )
            ]
        )
    fecha_nacimiento = forms.DateField(
            label='Fecha de Nacimiento', 
            widget=DatePickerInput(
                format='%Y-%m-%d',
                
            ),

        )

class EliminarEmpleadoForm(forms.Form):
    pk = forms.CharField()