from django.db import models
from django.urls import reverse
<<<<<<< HEAD
from encrypted_id.models import EncryptedIDModel

class Empleado(EncryptedIDModel):
=======

class Empleado(models.Model):
>>>>>>> 34c90082494e8267646737dfd0f3fe31ffaec890
    
    nombre = models.CharField(max_length=50)
    a_materno = models.CharField(max_length=50)
    a_paterno = models.CharField(max_length=50)
<<<<<<< HEAD
    fecha_nacimiento = models.DateField('Fecha de nacimiento')  
=======
    sexo = models.BooleanField()
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
>>>>>>> 34c90082494e8267646737dfd0f3fe31ffaec890
    fecha_registro = models.DateTimeField('Fecha de registro en el servidor')

    objects = models.Manager()
    
    #metodo que retorna el contenido del objeto
    def __str__(self):
        return '{0} {1} {2}'.format(self.nombre,self.a_paterno,self.a_materno)


# Create your models here.
