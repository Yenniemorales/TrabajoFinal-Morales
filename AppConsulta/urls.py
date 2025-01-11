from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('medico/', views.agregar_medico, name='agregar_medico'),
    path('consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('buscar/', views.buscar_consulta, name='buscar_consulta'),
]
