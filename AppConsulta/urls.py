from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para la página de inicio
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('agregar_medico/', views.agregar_medico, name='agregar_medico'),
    path('agregar_consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('buscar_consulta/', views.buscar_consulta, name='buscar_consulta'),
]
