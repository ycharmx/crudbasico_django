from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView, RedirectView, View
from apps.render_pdf.render import Render
from django.utils import timezone

from .models import Empleado
from .forms import EmpleadoForm, EmailForm, EliminarEmpleadoForm

class EmailView(TemplateView):
    template_name = 'crud/email.html'

    def get(self, request):
        form = EmailForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
        
        return HttpResponseRedirect('/empleados/')

class HomeView(TemplateView):
    template_name = 'crud/empleados.html'

    def get(self, request):
        empleados = Empleado.objects.order_by('-fecha_registro')
        return render(request,self.template_name,{'empleados':empleados})

class RegistrarEmpleadoView(TemplateView):
    template_name = 'crud/registrar.html'

    def get(self, request):
        form = EmpleadoForm()
        return render(request, self.template_name,{'form':form} )

    def post(self, request):
        if request.method == 'POST':
            form = EmpleadoForm(request.POST)
            if form.is_valid():
                empleado = Empleado()
                empleado.nombre = form.cleaned_data['nombre']
                empleado.a_materno = form.cleaned_data['a_materno']
                empleado.a_paterno = form.cleaned_data['a_paterno']
                empleado.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
                empleado.fecha_registro = timezone.now()
                empleado.sexo = True
                empleado.save()
                return HttpResponseRedirect('/empleados')
            else:
                return render(request, self.template_name, {'resultados' : 'El formulario no es valido'})

class EditarEmpleadoView(TemplateView):
    template_name = 'crud/editar.html'

    def get(self, request, pk):
        try:
            empleado = Empleado.objects.get(pk = pk)
            form = EmpleadoForm(initial={
                'nombre' : empleado.nombre, 
                'a_paterno' : empleado.a_paterno, 
                'a_materno' :  empleado.a_materno, 
                'fecha_nacimiento' : empleado.fecha_nacimiento,})
            return render(request, self.template_name, {'form' : form,})
        except Empleado.DoesNotExist:    
            self.pk = 0;
            return render(request, 'crud/excepciones.html', {'error' : 'La empleado no existe'})

    def post(self, request, pk):
        if request.method == 'POST':
            form = EmpleadoForm(request.POST)
            if form.is_valid():
                try:
                    empleado = get_object_or_404(Empleado,pk = pk)
                    empleado.nombre = form.cleaned_data['nombre']
                    empleado.a_paterno = form.cleaned_data['a_paterno']
                    empleado.a_materno = form.cleaned_data['a_materno']
                    empleado.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
                    empleado.save()
                    
                    form = EmpleadoForm(initial={
                        'nombre' : empleado.nombre, 
                        'a_paterno' : empleado.a_paterno, 
                        'a_materno' :  empleado.a_materno, 
                        'fecha_nacimiento' : empleado.fecha_nacimiento,}
                    )

                    return render(request, self.template_name, {'resultado' : 'Se ha actualizado el registro exitosamente','form' :form},)
                except Empleado.DoesNotExist:
                    return render(request, 'crud/excepciones.html', {'error' : 'El usuario que se intenta actualizar no existe'})
            else:
                return render(request, self.template_name, {'resultado' : 'Se ha actualizado el registro exitosamente'})

class EliminarEmpleadoView(TemplateView):
    
    def post(self, request):
        if request.method == 'POST':
            form = EliminarEmpleadoForm(request.POST)
            if form.is_valid():
                try:
                    pk = form.cleaned_data['pk']
                    empleado = get_object_or_404(Empleado,pk = pk)
                    empleado.delete()
                    return HttpResponseRedirect('/empleados')
                except Empleado.DoesNotExist:
                    return render(request,'crud/excepciones.html',{'error' : 'La empleado que desea eliminar no existe'})

class ReporteEmpleadosPDF(View):

    def get(self, request):
        empleados = Empleado.objects.order_by('-fecha_registro')
        fecha = timezone.now()
        correo = 'correo'
        params = {
            'email' : correo,
            'fecha' : fecha,
            'empleados': empleados,
        }
        return Render.render('render_pdf/rpt_empleados.html', params)


