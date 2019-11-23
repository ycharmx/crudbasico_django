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
    path('salir/', views.salir, name='salir')
]
