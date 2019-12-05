<<<<<<< HEAD
from django.urls import path, register_converter
from . import views

class ConvertEkey:
    regex = '[0-9a-zA-Z-_=]+'
    def to_python(self, value):
        return str(value)
    def to_url(self, value):
        return '%s' % value

register_converter(ConvertEkey, 'ekey')

app_name = 'crud'
urlpatterns = [
    path('',views.EmailView.as_view(),name='email'),
    path('empleados/',views.HomeView.as_view(), name = 'empleados'),
    path('empleados/agregar/', views.RegistrarEmpleadoView.as_view(), name='agregar_empleado'),
    path('empleados/editar/<ekey:pk>',views.EditarEmpleadoView.as_view(), name='editar_empleado'),
    path('empleados/eliminar/',views.EliminarEmpleadoView.as_view(),name = 'eliminar'),
    path('empleados/reporte/', views.ReporteEmpleadosPDF.as_view(), name = 'reporte_empleados'),
    path('empleados/reporte/<ekey:pk>', views.ReporteEmpleadoPDF.as_view(), name = 'reporte_empleado'),
=======
from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [

    path('',views.EmailView.as_view(),name='email'),
    path('empleados/',views.HomeView.as_view(), name = 'empleados'),
    path('empleados/agregar/', views.RegistrarEmpleadoView.as_view(), name='agregar_empleado'),
    path('empleados/<int:pk>/editar/',views.EditarEmpleadoView.as_view(), name='editar_empleado'),
    path('empleados/eliminar/',views.EliminarEmpleadoView.as_view(),name = 'eliminar'),
    path('empleados/reporte/', views.ReporteEmpleadosPDF.as_view(), name = 'reporte_empleados'),
>>>>>>> 34c90082494e8267646737dfd0f3fe31ffaec890
    path('salir/', views.salir, name='salir')
]
