from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Paciente, Medico, Consulta
from django.contrib import messages  # Sistema de mensajes
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserEditForm, ProfileEditForm

# VISTA: Home
@login_required
def home(request):
    total_pacientes = Paciente.objects.count()
    total_medicos = Medico.objects.count()
    total_consultas = Consulta.objects.count()

    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    consultas = Consulta.objects.all()

    registros_recientes = [
        {'tipo': 'Paciente', 'nombre': p.nombre, 'apellido': p.apellido, 'rut': p.rut}
        for p in Paciente.objects.order_by('-id')[:5]
    ] + [
        {'tipo': 'Médico', 'nombre': m.nombre, 'apellido': m.apellido, 'rut': m.rut}
        for m in Medico.objects.order_by('-id')[:5]
    ]

    return render(request, 'AppConsulta/home.html', {
        'total_pacientes': total_pacientes,
        'total_medicos': total_medicos,
        'total_consultas': total_consultas,
        'pacientes': pacientes,
        'medicos': medicos,
        'consultas': consultas,
        'registros_recientes': registros_recientes,
    })

# CRUD: Paciente
@login_required
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente guardado exitosamente.')
            return redirect('agregar_paciente')
    else:
        form = PacienteForm()

    return render(request, 'AppConsulta/agregar_paciente.html', {'form': form})

@login_required
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente actualizado correctamente.')
            return redirect('home')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'AppConsulta/agregar_paciente.html', {'form': form})

@login_required
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    messages.success(request, 'Paciente eliminado exitosamente.')
    return redirect('home')

# CRUD: Médico
@login_required
def agregar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico guardado exitosamente.')
            return redirect('agregar_medico')
    else:
        form = MedicoForm()
    return render(request, 'AppConsulta/agregar_medico.html', {'form': form})

@login_required
def editar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico actualizado correctamente.')
            return redirect('home')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'AppConsulta/agregar_medico.html', {'form': form})

@login_required
def eliminar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    medico.delete()
    messages.success(request, 'Médico eliminado exitosamente.')
    return redirect('home')

# CRUD: Consulta
@login_required
def agregar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.fecha_consulta = now()
            consulta.save()
            messages.success(request, 'Consulta guardada exitosamente.')
            return redirect('agregar_consulta')
    else:
        form = ConsultaForm()
    return render(request, 'AppConsulta/agregar_consulta.html', {'form': form})

@login_required
def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta actualizada correctamente.')
            return redirect('home')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'AppConsulta/agregar_consulta.html', {'form': form})

@login_required
def eliminar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    consulta.delete()
    messages.success(request, 'Consulta eliminada exitosamente.')
    return redirect('home')

# VISTA: Buscar Consulta
@login_required
def buscar_consulta(request):
    consultas = None
    if 'rut' in request.GET:  # Verifica si se envió el formulario
        rut = request.GET['rut']
        try:
            # Busca al paciente por RUT
            paciente = Paciente.objects.get(rut=rut)
            # Recupera las consultas relacionadas con el paciente
            consultas = Consulta.objects.filter(paciente=paciente)
        except Paciente.DoesNotExist:
            # Agrega un mensaje de error si no se encuentra el paciente
            messages.error(request, 'No se encontró un paciente con ese RUT.')
    return render(request, 'AppConsulta/buscar_consulta.html', {'consultas': consultas})


# Vista Personalizada de Logout
def custom_logout(request):
    logout(request)
    return redirect('login')

# Vista Personalizada de Registro
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            form = UserCreationForm()  # Generar un formulario vacío tras el registro
        else:
            messages.error(request, 'Hubo un error al registrar el usuario. Verifica los datos ingresados.')
    else:
        form = UserCreationForm()
    
    return render(request, 'AppConsulta/register.html', {'form': form})


@login_required
def editar_perfil(request):
    usuario = request.user  # Obtiene el usuario autenticado

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=usuario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            # Actualizar datos del usuario
            
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.email = informacion['email']

            # Cambiar contraseña si ambas coinciden y no están vacías
            if informacion.get('password1') and informacion['password1'] == informacion['password2']:
                usuario.set_password(informacion['password1'])
            elif informacion.get('password1') and informacion['password1'] != informacion['password2']:
                messages.error(request, 'Las contraseñas no coinciden.')
                return render(request, 'AppConsulta/editar_perfil.html', {"miFormulario": miFormulario})

            usuario.save()  # Guarda los cambios
            messages.success(request, 'Perfil actualizado correctamente.')
            #return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, 'AppConsulta/editar_perfil.html', {"miFormulario": miFormulario})

# Vista para editar el perfil
@login_required
def editar_perfil(request):
    usuario = request.user
    try:
        perfil = Profile.objects.get(user=usuario)
    except Profile.DoesNotExist:
        perfil = Profile.objects.create(user=usuario)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=usuario)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=perfil)  # Maneja archivos

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('home')  # Cambia según la URL de tu home
    else:
        user_form = UserEditForm(instance=usuario)
        profile_form = ProfileEditForm(instance=perfil)

    return render(request, "AppConsulta/editar_perfil.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })

def about(request):
    context = {
        'info': 'Esta aplicación está diseñada para gestionar pacientes, médicos y consultas de manera eficiente.',
        'features': [
            'Registro y administración de pacientes.',
            'Gestión de médicos y especialidades.',
            'Agendamiento y búsqueda de consultas.',
            'Registro y autenticación de usuarios.',
            'Edición de perfiles con avatares personalizados.'
        ],
        'team': 'Este proyecto fue desarrollado por Yennie Morales.',
        'score_range': range(5),  # Por ejemplo, un rango de 0 a 4
    }
    return render(request, 'AppConsulta/about.html', context)
