from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='AppConsulta/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # Registro de usuarios

    # Ruta principal
    path('', views.home, name='home'),

    # Rutas para pacientes
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('pacientes/<int:pk>/editar/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/<int:pk>/eliminar/', views.eliminar_paciente, name='eliminar_paciente'),

    # Rutas para médicos
    path('agregar_medico/', views.agregar_medico, name='agregar_medico'),
    path('medicos/<int:pk>/editar/', views.editar_medico, name='editar_medico'),
    path('medicos/<int:pk>/eliminar/', views.eliminar_medico, name='eliminar_medico'),

    # Rutas para consultas
    path('agregar_consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('consultas/<int:pk>/editar/', views.editar_consulta, name='editar_consulta'),
    path('consultas/<int:pk>/eliminar/', views.eliminar_consulta, name='eliminar_consulta'),

    # Búsqueda de consultas
    path('buscar_consulta/', views.buscar_consulta, name='buscar_consulta'),
]

