#Importamos la opcion para validar la existencia del objeto ==> get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

#importamos el modelo persona que se ha creado
from .models import Persona

def inicio(req):
    return HttpResponse("Hola mundo")

#método para listar las personas
def listar(req):
    lista_personas = Persona.objects.order_by("-fecha_registro")
    # resultado = ','.join([p.nombre for p in lista_personas])
    context = {'personas' : lista_personas}
    return render(req,'crud/listar.html',context)

def crear(req):
    return HttpResponse()

def editar(req, id_persona):
    try:
        persona = get_object_or_404(Persona, pk=id_persona)
        context = {'persona':persona}
    except Persona.DoesNotExist:
        raise Http404("La persona no existe")
    return render(req,'crud/editar.html',context)

def eliminar(req, id_persona):
    return HttpResponse()

# Create your views here.
