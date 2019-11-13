from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar),
    path('editar/<int:id_persona>/',views.editar)
]
