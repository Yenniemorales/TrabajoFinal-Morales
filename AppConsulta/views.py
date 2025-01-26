from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm, MedicoForm, ConsultaForm
from .models import Paciente, Medico, Consulta
from django.contrib import messages  # Sistema de mensajes
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
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
    if 'rut' in request.GET:
        rut = request.GET['rut']
        try:
            paciente = Paciente.objects.get(rut=rut)
            consultas = Consulta.objects.filter(paciente=paciente)
        except Paciente.DoesNotExist:
            messages.error(request, 'No se encontró un paciente con ese RUT.', extra_tags='buscar_consulta')
    return render(request, 'AppConsulta/buscar_consulta.html', {'consultas': consultas})

# Vista de Registro
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
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'AppConsulta/register.html', {'form': form})