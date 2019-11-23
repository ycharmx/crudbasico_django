from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView, RedirectView, View
from django.utils import timezone

from apps.render_pdf.render import Render
from apps.email_exceptions.send_email import NotificarException
from crudbasico.base import LoadConfig
from django.core.mail import EmailMessage, send_mail

from .models import Empleado    
from .forms import EmpleadoForm, EmailForm, EliminarEmpleadoForm
from apps.email_exceptions.email_connection import EmailConnection

# json_config = LoadConfig('apps_config.json')
# email_server = EmailConnection()
# email_server.start_smtp(json_config.get_env_var('email'), json_config.get_env_var('password'))


# Formato de uso para el servicio de gmail
# ----------------------------------------------------------------------------------------------
# excepcion.enviar_mensaje(
#     timezone.now(),
#     'crud.views %s method:get' % (self.template_name),
#     'Excepcion en la pagina de la aodijasdoij'
# )

excepcion = NotificarException()

class EmailView(TemplateView):
    template_name = 'crud/email.html'

    def get(self, request):
        try:  
            if 'email' in request.session:
                return HttpResponseRedirect('/empleados/')
            else:
                form = EmailForm()  
                return render(request, self.template_name, {'form':form})
        except Exception as e:
            excepcion.enviar_mensaje(
                'crud.views.EmailView %s method:get' % (self.template_name),
                '%s' % (str(e))
            )

    def post(self, request):
        try:
            form = EmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                request.session['email'] = email
                return HttpResponseRedirect('/empleados/')
            else:
                return render(request, self.template_name, {'form': form, 'error' : 'Ingrese un correo valido'})
        except Exception as e:
            excepcion.enviar_mensaje(
                'crud.views.EmailView %s method:post' % (self.template_name),
                '%s' % (str(e))
            )

class HomeView(TemplateView):
    template_name = 'crud/empleados.html'

    def get(self, request):
        try:
            if 'email' in request.session:
                email = request.session['email']
                empleados = Empleado.objects.order_by('-fecha_registro')
                return render(request,self.template_name,{'empleados':empleados, 'email': email})
            else:
                return HttpResponseRedirect("/")   
        except Exception as e:
            excepcion.enviar_mensaje(
                'crud.views.HomeView %s method:get' % (self.template_name),
                '%s' % (str(e))
            )
        
class RegistrarEmpleadoView(TemplateView):
    template_name = 'crud/registrar.html'

    def get(self, request):
        try:
            if 'email' in request.session:
                email = request.session['email']
                form = EmpleadoForm()
                return render(request, self.template_name,{'form':form, 'email' : email} )
            else:
                return HttpResponseRedirect("/")   
        except Exception as e:
            excepcion.enviar_mensaje(
                'crud.views.RegistrarEmpleadoView %s method:get' % (self.template_name),
                '%s' % (str(e))
            )
       
    def post(self, request):
        try:
            if 'email' in request.session:
                email = request.session['email']
                if request.method == 'POST':
                    form = EmpleadoForm(request.POST)
                    if form.is_valid():
                        empleado = Empleado()
                        empleado.nombre = str.strip(form.cleaned_data['nombre'])
                        empleado.a_materno = str.strip(form.cleaned_data['a_materno'])
                        empleado.a_paterno = str.strip(form.cleaned_data['a_paterno'])
                        empleado.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
                        empleado.fecha_registro = timezone.now()
                        empleado.sexo = True
                        empleado.save()
                        return HttpResponseRedirect('/empleados')
                    else:
                        return render(request, self.template_name, 
                            {   'form' :form, 
                                'error' : 'El formulario no es valido, revise los datos que está tratando de ingresar',
                                'email' : email
                            }
                        )
            else:
                return HttpResponseRedirect("/")   
        except Exception as e:
            excepcion.enviar_mensaje(
                'crud.views.RegistrarEmpleadoView %s method:post' % (self.template_name),
                '%s' % (str(e))
            )

class EditarEmpleadoView(TemplateView):
    template_name = 'crud/editar.html'

    def get(self, request, pk):
        try:
            if 'email' in request.session:
                email = request.session['email']
                empleado = Empleado.objects.get(pk = pk)
                form = EmpleadoForm(initial={
                    'nombre' : str.strip(empleado.nombre), 
                    'a_paterno' : str.strip(empleado.a_paterno), 
                    'a_materno' :  str.strip(empleado.a_materno), 
                    'fecha_nacimiento' : empleado.fecha_nacimiento,})
                return render(request, self.template_name, 
                    {
                        'form' : form,
                        'email' : email
                    }
                )
            else:
                return HttpResponseRedirect("/")
        except Empleado.DoesNotExist:    
            raise Http404()

    def post(self, request, pk):
        try:
            if 'email' in request.session:
                email = request.session['email']

                if request.method == 'POST':
                    form = EmpleadoForm(request.POST)
                    if form.is_valid():

                            empleado = get_object_or_404(Empleado,pk = pk)
                            empleado.nombre = str.strip(form.cleaned_data['nombre'])
                            empleado.a_paterno = str.strip(form.cleaned_data['a_paterno'])
                            empleado.a_materno = str.strip(form.cleaned_data['a_materno'])
                            empleado.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
                            empleado.save()
                            
                            form = EmpleadoForm(initial={
                                'nombre' : empleado.nombre, 
                                'a_paterno' : empleado.a_paterno, 
                                'a_materno' :  empleado.a_materno, 
                                'fecha_nacimiento' : empleado.fecha_nacimiento,}
                            )

                            return render(request, self.template_name, 
                                {
                                    'resultado' : 'Se ha actualizado el registro exitosamente',
                                    'form' :form,
                                    'email':email
                                }
                            )
                    else:
                        return render(request, self.template_name, 
                            {
                                'error' : 'El formulario no es valido, revise los datos que está tratando de ingresar',
                                'email' : email,
                                'form' : form
                            }
                        )
        
            else:
                return HttpResponseRedirect("/")
           
        except Exception as e:
            # excepcion.enviar_mensaje(
            #     'crud.views.EditarEmpleadoView %s method:post' % (self.template_name),
            #     '%s' % (str(e))
            # )
            raise Http404()

class EliminarEmpleadoView(TemplateView):
    
    def post(self, request):
        try:
            if 'email' in request.session:
                if request.method == 'POST':
                    form = EliminarEmpleadoForm(request.POST)
                    if form.is_valid():
                        try:
                            pk = form.cleaned_data['pk']
                            empleado = get_object_or_404(Empleado,pk = pk)
                            empleado.delete()
                            return HttpResponseRedirect('/empleados/')
                        except Empleado.DoesNotExist:
                            return HttpResponseRedirect("/empleados/")
            else:
                return HttpResponseRedirect('/')
            
        except Exception as e:
            # excepcion.enviar_mensaje(
            #     'crud.views.EliminarEmpleadoView %s method:post' % (self.template_name),
            #     '%s' % (str(e))
            # )
            raise Http404()

class ReporteEmpleadosPDF(View):

    def get(self, request):
        try:
            if 'email' in request.session:
                empleados = Empleado.objects.order_by('-fecha_registro')
                fecha = timezone.now()
                email = request.session['email']
                params = {
                    'email' : email,
                    'fecha' : fecha,
                    'empleados': empleados,
                }
                return Render.render('render_pdf/rpt_empleados.html', params)
            else:
                return HttpResponseRedirect("/")

        except Exception as e:
            excepcion.enviar_mensaje(
                'crud.views.ReporteEmpleadoView %s method:ge' % (self.template_name),
                '%s' % (str(e))
            )

def salir(request):
    if 'email' in request.session:
        del request.session['email']
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/empleados/")