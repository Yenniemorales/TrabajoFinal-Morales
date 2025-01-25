from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm, MedicoForm, ConsultaForm
from .models import Paciente, Medico, Consulta
from django.utils.timezone import is_naive, make_aware
from pytz import timezone
from django.contrib import messages  # Importa el sistema de mensajes
from django.utils.timezone import now

# VISTA: home
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
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente guardado exitosamente.')  # Mensaje de éxito
            return redirect('agregar_paciente')
    else:
        form = PacienteForm()

    return render(request, 'AppConsulta/agregar_paciente.html', {'form': form})

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'AppConsulta/agregar_paciente.html', {'form': form})

def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('home')


# CRUD: Medico
def agregar_medico(request):
    """
    Vista para agregar un nuevo médico con mensaje de confirmación.
    """
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico guardado exitosamente.')  # Mensaje de éxito
            return redirect('agregar_medico')
    else:
        form = MedicoForm()
    return render(request, 'AppConsulta/agregar_medico.html', {'form': form})


def editar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'AppConsulta/agregar_medico.html', {'form': form})

def eliminar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    medico.delete()
    return redirect('home')


# CRUD: Consulta
def agregar_consulta(request):
    """
    Vista para agregar una nueva consulta con la hora detectada automáticamente.
    """
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)  # Crear consulta sin guardarla aún
            consulta.fecha_consulta = now()  # Asignar la fecha y hora actual automáticamente
            consulta.save()  # Guardar la consulta
            messages.success(request, 'Consulta guardada exitosamente con la fecha y hora actuales.')
            return redirect('agregar_consulta')
    else:
        form = ConsultaForm()

    return render(request, 'AppConsulta/agregar_consulta.html', {'form': form})

def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'AppConsulta/agregar_consulta.html', {'form': form})

def eliminar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    consulta.delete()
    return redirect('home')


# VISTA: buscar_consulta
def buscar_consulta(request):
    consultas = None
    if 'rut' in request.GET:
        rut = request.GET['rut']
        try:
            paciente = Paciente.objects.get(rut=rut)
            consultas = Consulta.objects.filter(paciente=paciente)
        except Paciente.DoesNotExist:
            consultas = []
    return render(request, 'AppConsulta/buscar_consulta.html', {'consultas': consultas})
