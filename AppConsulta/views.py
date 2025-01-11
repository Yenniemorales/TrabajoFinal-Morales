from django.shortcuts import render, redirect
from .forms import PacienteForm, MedicoForm, ConsultaForm
from .models import Paciente, Medico, Consulta
from django.http import HttpResponse
from datetime import date, datetime
import pytz

# Vista para la página de inicio
def home(request):
    # Obtenemos los totales y últimos pacientes registrados
    total_pacientes = Paciente.objects.count()
    total_medicos = Medico.objects.count()
    total_consultas = Consulta.objects.count()
    pacientes_recientes = Paciente.objects.order_by('-id')[:5]

    # Renderizamos la plantilla con el contexto
    return render(request, 'AppConsulta/home.html', {
        'total_pacientes': total_pacientes,
        'total_medicos': total_medicos,
        'total_consultas': total_consultas,
        'pacientes_recientes': pacientes_recientes,
    })

# Vista para agregar paciente
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_paciente')  # Redirige a la misma página
    else:
        form = PacienteForm()
    return render(request, 'AppConsulta/agregar_paciente.html', {'form': form})

# Vista para agregar médico
def agregar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_medico')  # Redirige a la misma página
    else:
        form = MedicoForm()
    return render(request, 'AppConsulta/agregar_medico.html', {'form': form})

# Vista para agregar consulta
def agregar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)

            # Procesar la fecha de consulta
            fecha_consulta = form.cleaned_data['fecha_consulta']
            if isinstance(fecha_consulta, date):  # Si es una fecha sin tiempo
                fecha_consulta = datetime.combine(fecha_consulta, datetime.min.time())  # Agregar tiempo mínimo
                
                # Agregar zona horaria (opcional)
                timezone = pytz.timezone('America/Santiago')
                fecha_consulta = timezone.localize(fecha_consulta)

            consulta.fecha_consulta = fecha_consulta
            consulta.save()
            return redirect('agregar_consulta')  # Redirige después de guardar
    else:
        form = ConsultaForm()
    return render(request, 'AppConsulta/agregar_consulta.html', {'form': form})

# Vista para buscar consultas
def buscar_consulta(request):
    consultas = None
    if 'q' in request.GET:
        query = request.GET['q']
        consultas = Consulta.objects.filter(motivo__icontains=query)  # Filtra por el motivo
    return render(request, 'AppConsulta/buscar_consulta.html', {'consultas': consultas})
