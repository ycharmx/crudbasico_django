from django.shortcuts import render
from django.http import HttpResponse

#importamos el modelo persona que se ha creado
from .models import Persona

def inicio(req):
    return HttpResponse("Hola mundo")

#método para listar las personas
def listar(req):
    lista_personas = Persona.objects.order_by("-fecha_registro")
    resultado = ','.join([p.nombre for p in lista_personas])
    return HttpResponse(resultado)
# Create your views here.
