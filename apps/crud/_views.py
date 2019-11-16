import io
#Importamos la opcion para validar la existencia del objeto ==> get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, FileResponse
from django.views import generic
#importamos el modelo persona que se ha creado
from .models import Empleado

#importamos las formas para renderizar los formularios
from .forms import EmailForm, RegistroPersonaForm

from reportlab.pdfgen import canvas
# def inicio(req):
#     return HttpResponse("Hola mundo")

# #método para listar las personas
def listar(req):
    lista_empleado = Empleado.objects.order_by("-fecha_registro")
        # resultado = ','.join([p.nombre for p in lista_empleado])
    context = {'personas' : lista_empleado}
    if req.method == 'POST':
        print(req.POST.get('pk'))
        return render(req,'crud/listar.html',context)
    else:
        return render(req,'crud/listar.html',context)
     
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

def eliminar(req):
    if req.method == 'POST':
        pk=int(req.POST.get('pk',0))
        print(req.POST.get('pk'))
        try:
            persona = get_object_or_404(Empleado.objects.get(pk=pk))      
            persona.delete();
            return HttpResponseRedirect('/personas/')
        except Empleado.DoesNotExist:
            return HttpResponseRedirect('/personas/',{'error':'La persona no existe'})
        # delete an object and send a confirmation respons
    return HttpResponseRedirect('/personas/')

def crear(req):
    form = RegistroPersonaForm()
    if req.method == "POST":
        form = RegistroPersonaForm(req.POST)
        if form.is_valid():
            persona = Empleado()
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

def generar_pdf(req, id_persona):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 100, "Hello world.")
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

# def eliminar(req):
#     if req.method == 'POST':
    

class ListarView(generic.ListView):
    template_name = 'crud/listar.html'
    context_object_name = 'personas'
    
    def get_queryset(self):
        return Empleado.objects.order_by("-fecha_registro")

class EditarView(generic.DetailView):
    model = Empleado
    template_name = "crud/editar.html"
    context_object_name = 'persona'

# Create your views here.
