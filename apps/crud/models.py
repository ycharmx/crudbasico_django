from django.db import models
from django.urls import reverse

class Persona(models.Model):
    nombre = models.CharField(_(""), max_length=50)
    a_materno = models.CharField(max_length=50)
    a_paterno = models.CharField(max_length=50)
    sexo = models.BooleanField()
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    fecha_registro = models.DateTimeField('Fecha de registro en el servidor')

    #metodo que retorna el contenido del objeto
    def __str__(self):
        return self.nombre


# Create your models here.
