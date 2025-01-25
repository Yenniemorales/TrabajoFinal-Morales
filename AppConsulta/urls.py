from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('pacientes/<int:pk>/editar/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/<int:pk>/eliminar/', views.eliminar_paciente, name='eliminar_paciente'),
    path('agregar_medico/', views.agregar_medico, name='agregar_medico'),
    path('medicos/<int:pk>/editar/', views.editar_medico, name='editar_medico'),
    path('medicos/<int:pk>/eliminar/', views.eliminar_medico, name='eliminar_medico'),
    path('agregar_consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('consultas/<int:pk>/editar/', views.editar_consulta, name='editar_consulta'),
    path('consultas/<int:pk>/eliminar/', views.eliminar_consulta, name='eliminar_consulta'),
    path('buscar_consulta/', views.buscar_consulta, name='buscar_consulta'),
]
