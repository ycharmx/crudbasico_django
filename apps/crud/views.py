#Importamos la opcion para validar la existencia del objeto ==> get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
#importamos el modelo persona que se ha creado
from .models import Persona

# def inicio(req):
#     return HttpResponse("Hola mundo")

# #método para listar las personas
# def listar(req):
#     lista_personas = Persona.objects.order_by("-fecha_registro")
#     # resultado = ','.join([p.nombre for p in lista_personas])
#     context = {'personas' : lista_personas}
#     return render(req,'crud/listar.html',context)


def crear(req):
    return render(req,'crud/registrar.html')

# def editar(req, id_persona):
#     try:
#         persona = get_object_or_404(Persona, pk=id_persona)
#         context = {'persona':persona}
#     except Persona.DoesNotExist:
#         raise Http404("La persona no existe")
#     return render(req,'crud/editar.html',context)

# def eliminar(req, id_persona):
#     try:
#         persona = get_object_or_404(Persona,pk=id_persona)
#     except Persona.DoesNotExist:
#         raise Http404("La persona no existe")
#     return HttpResponse()

class ListarView(generic.ListView):
    template_name = 'crud/listar.html'
    context_object_name = 'personas'
    def get_queryset(self):
        return Persona.objects.order_by("-fecha_registro")

class EditarView(generic.DetailView):
    model = Persona
    template_name = "crud/editar.html"
    context_object_name = 'persona'

# Create your views here.
