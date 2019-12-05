from django import forms
<<<<<<< HEAD
from django.core.validators import RegexValidator
from bootstrap_datepicker_plus import DatePickerInput, YearPickerInput
import datetime

input_attrs = {'class' : 'form-control text-left mb-2'}
regex_only_letters =  RegexValidator(
                        regex = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$",
                        message = "Sólo letras"
                     )
=======

#importamos el modelo de persona
from .models import Empleado
from django.core.validators import RegexValidator
from bootstrap_datepicker_plus import DatePickerInput

input_attrs = {'class' : 'form-control text-left mb-2'}
>>>>>>> 34c90082494e8267646737dfd0f3fe31ffaec890

class EmailForm(forms.Form):
    email = forms.CharField(
            label='Correo Electrónico', max_length=30,widget=forms.TextInput(input_attrs),
            validators=[
                RegexValidator(
                    regex="^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",

                )
<<<<<<< HEAD
            ]            
        )

class EmpleadoForm(forms.Form):
    
    fecha = datetime.datetime.now()
    
    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fecha = datetime.datetime.now()
        print(self.fecha.year)
    
    nombre = forms.CharField(
            label='Nombre', max_length=50,widget=forms.TextInput(input_attrs),
            validators = [ regex_only_letters ]            
=======
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
>>>>>>> 34c90082494e8267646737dfd0f3fe31ffaec890
        )
    a_paterno = forms.CharField(
            label='Apellido Paterno', max_length=50,widget=forms.TextInput(input_attrs),
             validators = [
<<<<<<< HEAD
               
=======
                RegexValidator(
                    regex = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$",
                    message = "Sólo letras"
                )
>>>>>>> 34c90082494e8267646737dfd0f3fe31ffaec890
            ]
        )
    a_materno = forms.CharField(
            label='Apellido Materno', max_length=50,widget=forms.TextInput(input_attrs),
<<<<<<< HEAD
            validators = [ regex_only_letters ]            
=======
             validators = [
                RegexValidator(
                    regex = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$",
                    message = "Sólo letras"
                )
            ]
>>>>>>> 34c90082494e8267646737dfd0f3fe31ffaec890
        )
    fecha_nacimiento = forms.DateField(
            label='Fecha de Nacimiento', 
            widget=DatePickerInput(
<<<<<<< HEAD
                options={
                    "format":'YYYY-MM-DD',    
                    "minDate":"%s-01-01" % (fecha.year-140),
                    "maxDate":"%s-%s-%s" % (fecha.year,fecha.month,fecha.day),
                    "viewMode":'years',
                    "useCurrent":False,
                    "defaultDate":"%s-01-01" % (fecha.year-70)
                }
            ),
        )

class EliminarEmpleadoForm(forms.Form):
    pk = forms.CharField()
=======
                format='%Y-%m-%d',
                
            ),

        )

class EliminarEmpleadoForm(forms.Form):
    pk = forms.IntegerField()
>>>>>>> 34c90082494e8267646737dfd0f3fe31ffaec890
