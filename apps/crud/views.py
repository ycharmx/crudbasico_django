#Importamos la opcion para validar la existencia del objeto ==> get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
#importamos el modelo persona que se ha creado
from .models import Persona

#importamos las formas para renderizar los formularios
from .forms import EmailForm, RegistroPersonaForm

# def inicio(req):
#     return HttpResponse("Hola mundo")

# #método para listar las personas
# def listar(req):
#     lista_personas = Persona.objects.order_by("-fecha_registro")
#     # resultado = ','.join([p.nombre for p in lista_personas])
#     context = {'personas' : lista_personas}
#     return render(req,'crud/listar.html',context)

def email(req):
    if req.method == "POST":
        form = EmailForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # personas = Persona.objects.order_by("-fecha_registro")
            # return render(req, 'crud/listar.html',{'email':email, 'personas':personas})
            return HttpResponseRedirect('personas/')
    else:
        form = EmailForm()
    return render(req,'crud/email.html', {'form':form})


def crear(req):
    form = RegistroPersonaForm()
    if req.method == "POST":
        form = RegistroPersonaForm(req.POST)
        if form.is_valid():
            persona = Persona()
            persona.nombre = form.cleaned_data['nombre']
            persona.a_materno = form.cleaned_data['a_materno']
            persona.a_paterno = form.cleaned_data['a_paterno']
            persona.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            persona.fecha_registro = form.cleaned_data['fecha_nacimiento']
            persona.sexo = True
            persona.save()
            return HttpResponseRedirect('/personas/')
        else:
            return render (req,'crud/registrar.html',{'form':form})
        
    return render(req,'crud/registrar.html',{'form':form})

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
