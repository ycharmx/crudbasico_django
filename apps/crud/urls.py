from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [

    # path('',views.listar),
    # path('editar/<int:id_persona>/',views.editar),
    # path('registrar/',views.crear),
    # path('eliminar/<int:id_persona>',views.eliminar)

    path('',views.ListarView.as_view(), name = 'listar'),
    path('editar/<int:pk>/',views.EditarView.as_view(), name = 'editar'),
    path('agregar/',views.crear, name = 'agregar')
]
