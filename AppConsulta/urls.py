from django.urls import path
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django
from . import views  # Importa tus vistas personalizadas

urlpatterns = [
    # Ruta para la página principal
    path('', views.home, name='home'),

    # Ruta para editar perfil
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),

    # CRUD: Pacientes
    path('agregar_paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('editar_paciente/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar_paciente/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),

    # CRUD: Médicos
    path('agregar_medico/', views.agregar_medico, name='agregar_medico'),
    path('editar_medico/<int:pk>/', views.editar_medico, name='editar_medico'),
    path('eliminar_medico/<int:pk>/', views.eliminar_medico, name='eliminar_medico'),

    # CRUD: Consultas
    path('agregar_consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('editar_consulta/<int:pk>/', views.editar_consulta, name='editar_consulta'),
    path('eliminar_consulta/<int:pk>/', views.eliminar_consulta, name='eliminar_consulta'),

    # Buscar Consulta
    path('buscar_consulta/', views.buscar_consulta, name='buscar_consulta'),

    # Registro y logout
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),

    # Login
    path('login/', auth_views.LoginView.as_view(template_name='AppConsulta/login.html'), name='login'),

    # Ruta About
    path('about/', views.about, name='about'),  # Nueva ruta para "about"
]
