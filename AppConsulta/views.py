from django.shortcuts import render, redirect
from .forms import PacienteForm, MedicoForm, ConsultaForm
from .models import Consulta
from django.http import HttpResponse
from django.shortcuts import render  # Importa la función render para renderizar plantillas
from .models import Paciente, Medico, Consulta  # Importa los modelos utilizados en esta vista
from datetime import datetime
import pytz 
# Vista para la página de inicio
def home(request):
    # Cuenta el total de pacientes registrados en la base de datos
    total_pacientes = Paciente.objects.count()
    
    # Cuenta el total de médicos registrados en la base de datos
    total_medicos = Medico.objects.count()
    
    # Cuenta el total de consultas agendadas en la base de datos
    total_consultas = Consulta.objects.count()
    
    # Obtiene los últimos 5 pacientes registrados, ordenados por ID de forma descendente
    pacientes_recientes = Paciente.objects.order_by('-id')[:5]

    # Renderiza la plantilla 'home.html' y pasa los datos como contexto
    return render(request, 'AppConsulta/home.html', {
        'total_pacientes': total_pacientes,  # Total de pacientes registrados
        'total_medicos': total_medicos,      # Total de médicos registrados
        'total_consultas': total_consultas,  # Total de consultas agendadas
        'pacientes_recientes': pacientes_recientes,  # Lista de los últimos 5 pacientes
    })

#Creo vista para agregar paciente
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_paciente')
    else:
        form = PacienteForm()
    return render(request, 'AppConsulta/agregar_paciente.html', {'form': form})

#Creo vista para agregar medico
def agregar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_medico')  # Redirige a la misma página para nuevas entradas
    else:
        form = MedicoForm()  # Formulario vacío para GET
    return render(request, 'AppConsulta/agregar_medico.html', {'form': form})

#Creo vista para agregar consulta
# Vista para agregar consulta
def agregar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            
            # Obtener la fecha de consulta del formulario
            fecha_consulta = form.cleaned_data['fecha_consulta']
            
            # Si la fecha solo tiene el formato de fecha (sin hora), la convertimos a datetime
            if isinstance(fecha_consulta, datetime.date):
                # Combinamos la fecha con la hora mínima (00:00:00)
                fecha_consulta = datetime.combine(fecha_consulta, datetime.min.time())
                
                # Si es necesario, agregar la zona horaria
                timezone = pytz.timezone('America/New_York')  # Cambia a la zona horaria deseada
                fecha_consulta = timezone.localize(fecha_consulta)  # Convertir a aware datetime

            consulta.fecha_consulta = fecha_consulta
            consulta.save()  # Guardamos la consulta con la fecha correctamente procesada
            
            return redirect('agregar_consulta')  # Redirige después de guardar
    else:
        form = ConsultaForm()
    return render(request, 'AppConsulta/agregar_consulta.html', {'form': form})


#Creo vista para buscar consulta
def buscar_consulta(request):
    consultas = None
    if 'q' in request.GET:
        query = request.GET['q']
        consultas = Consulta.objects.filter(motivo__icontains=query)
    return render(request, 'AppConsulta/buscar_consulta.html', {'consultas': consultas})
