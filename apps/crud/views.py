from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView, RedirectView


from .models import Persona
from .forms import PersonaForm, EmailForm, EliminarPersonaForm

class EmailView(TemplateView):
    template_name = 'crud/email.html'

    def get(selft, request):
        form = EmailForm()
        return render(request, selft.template_name, {'form':form})
    
    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
        
        return HttpResponseRedirect('/personas/')

class HomeView(TemplateView):
    template_name = 'crud/personas.html'

    def get(self, request):
        personas = Persona.objects.order_by('-fecha_registro')
        return render(request,self.template_name,{'personas':personas})

class RegistrarPersonaView(TemplateView):
    template_name = 'crud/registrar.html'

    def get(self, request):
        form = PersonaForm()
        return render(request, self.template_name,{'form':form} )

    def post(self, request):
        if request.method == 'POST':
            form = PersonaForm(request.POST)
            if form.is_valid():
                persona = Persona()
                persona.nombre = form.cleaned_data['nombre']
                persona.a_materno = form.cleaned_data['a_materno']
                persona.a_paterno = form.cleaned_data['a_paterno']
                persona.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
                persona.fecha_registro = form.cleaned_data['fecha_nacimiento']
                persona.sexo = True
                persona.save()
                return HttpResponseRedirect('/personas')
            else:
                return render(request, self.template_name, {'resultados' : 'El formulario no es valido'})

class EditarPersonaView(TemplateView):
    template_name = 'crud/editar.html'

    def get(self, request, pk):
        try:
            persona = Persona.objects.get(pk = pk)
            form = PersonaForm(initial={
                'nombre' : persona.nombre, 
                'a_paterno' : persona.a_paterno, 
                'a_materno' :  persona.a_materno, 
                'fecha_nacimiento' : persona.fecha_nacimiento,})
            return render(request, self.template_name, {'form' : form,})
        except Persona.DoesNotExist:    
            self.pk = 0;
            return render(request, 'crud/excepciones.html', {'error' : 'La persona no existe'})

    def post(self, request, pk):
        if request.method == 'POST':
            form = PersonaForm(request.POST)
            if form.is_valid():
                try:
                    persona = get_object_or_404(Persona,pk = pk)
                    persona.nombre = form.cleaned_data['nombre']
                    persona.a_paterno = form.cleaned_data['a_paterno']
                    persona.a_materno = form.cleaned_data['a_materno']
                    persona.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
                    persona.save()
                    
                    form = PersonaForm(initial={
                        'nombre' : persona.nombre, 
                        'a_paterno' : persona.a_paterno, 
                        'a_materno' :  persona.a_materno, 
                        'fecha_nacimiento' : persona.fecha_nacimiento,}
                    )

                    return render(request, self.template_name, {'resultado' : 'Se ha actualizado el registro exitosamente','form' :form},)
                except Persona.DoesNotExist:
                    return render(request, 'crud/excepciones.html', {'error' : 'El usuario que se intenta actualizar no existe'})
            else:
                return render(request, self.template_name, {'resultado' : 'Se ha actualizado el registro exitosamente'})

class EliminarPersonaView(TemplateView):
    
    def post(self, request):
        if request.method == 'POST':
            form = EliminarPersonaForm(request.POST)
            if form.is_valid():
                try:
                    pk = form.cleaned_data['pk']
                    persona = get_object_or_404(Persona,pk = pk)
                    persona.delete()
                    return HttpResponseRedirect('/personas')
                except Persona.DoesNotExist:
                    return render(request,'crud/excepciones.html',{'error' : 'La persona que desea eliminar no existe'})



