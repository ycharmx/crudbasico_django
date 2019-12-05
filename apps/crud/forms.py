from django import forms
from django.core.validators import RegexValidator
from bootstrap_datepicker_plus import DatePickerInput, YearPickerInput
import datetime

input_attrs = {'class' : 'form-control text-left mb-2'}
regex_only_letters =  RegexValidator(
                        regex = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$",
                        message = "Sólo letras"
                     )

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
    
    fecha = datetime.datetime.now()
    
    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fecha = datetime.datetime.now()
        print(self.fecha.year)
    
    nombre = forms.CharField(
            label='Nombre', max_length=50,widget=forms.TextInput(input_attrs),
            validators = [ regex_only_letters ]            
        )
    a_paterno = forms.CharField(
            label='Apellido Paterno', max_length=50,widget=forms.TextInput(input_attrs),
             validators = [
               
            ]
        )
    a_materno = forms.CharField(
            label='Apellido Materno', max_length=50,widget=forms.TextInput(input_attrs),
            validators = [ regex_only_letters ]            
        )
    fecha_nacimiento = forms.DateField(
            label='Fecha de Nacimiento', 
            widget=DatePickerInput(
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
<<<<<<< HEAD
    pk = forms.CharField()
=======
    pk = forms.CharField()
>>>>>>> master
