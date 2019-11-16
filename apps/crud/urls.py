from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [

    path('',views.EmailView.as_view(),name='email'),
    path('personas/',views.HomeView.as_view(), name = 'personas'),
    path('personas/agregar/', views.RegistrarPersonaView.as_view(), name='agregar_persona'),
    path('personas/<int:pk>/editar/',views.EditarPersonaView.as_view(), name='editar_persona'),
    path('eliminar/',views.EliminarPersonaView.as_view(),name = 'eliminar')
    # path('editar/<int:pk>/',views.EditarView.as_view(), name = 'editar'),
    # path('agregar/',views.crear, name = 'agregar'),
    # path('eliminar/',views.eliminar,name='eliminar'),
    # path('generar_pdf/',views.generar_pdf,name ='generar_pdf')
]
