from django.shortcuts import render, redirect
from .forms import PacienteForm, MedicoForm, ConsultaForm
from .models import Paciente, Medico, Consulta
from django.http import HttpResponse
from datetime import date, datetime
from django.utils.timezone import is_naive, make_aware, now
from pytz import timezone


# VISTA: home
def home(request):
    """
    Vista principal (home) que muestra información general como:
    - Totales de pacientes, médicos, consultas
    - Últimos registros (pacientes y médicos) con su tipo
    """
    # Obtengo la cantidad total de pacientes, médicos y consultas
    total_pacientes = Paciente.objects.count()
    total_medicos = Medico.objects.count()
    total_consultas = Consulta.objects.count()

    # Obtengo los últimos pacientes (ordenados por '-id') y médicos
    pacientes = Paciente.objects.order_by('-id')[:5]  # Últimos 5 pacientes
    medicos = Medico.objects.order_by('-id')[:5]  # Últimos 5 médicos

    # Combino pacientes y médicos en una sola lista
    registros_recientes = []

    # Agrego pacientes a la lista con su etiqueta
    for p in pacientes:
        registros_recientes.append({
            'tipo': 'Paciente',  # Indica que es un paciente
            'nombre': p.nombre,
            'apellido': p.apellido,
            'rut': p.rut,
        })

    # Agrego médicos a la lista con su etiqueta
    for m in medicos:
        registros_recientes.append({
            'tipo': 'Médico',  # Indica que es un médico
            'nombre': m.nombre,
            'apellido': m.apellido,
            'rut': m.rut,
        })

    return render(request, 'AppConsulta/home.html', {
        'total_pacientes': total_pacientes,
        'total_medicos': total_medicos,
        'total_consultas': total_consultas,
        'registros_recientes': registros_recientes, 
    })

#     VISTA: agregar_paciente
def agregar_paciente(request):
    """
    Vista que maneja el formulario para agregar un nuevo Paciente.
    Si el método de la request es POST, intentamos validar y guardar el formulario.
    Si es GET, se muestra el formulario vacío.
    """
    if request.method == 'POST':
        # Si el método es POST, significa que estamos recibiendo datos del formulario.
        form = PacienteForm(request.POST)  # Creamos una instancia del formulario con la data recibida.
        if form.is_valid():
            # Si el formulario es válido según las validaciones de Django,
            # se guarda el paciente en la base de datos.
            form.save()
            # Después de guardar, redirigimos a la misma página
            return redirect('agregar_paciente')
    else:
        # Si el método NO es POST (ej. GET), se crea el formulario vacío.
        form = PacienteForm()
 
    return render(request, 'AppConsulta/agregar_paciente.html', {'form': form})


#     VISTA: agregar_medico
def agregar_medico(request):
    """
    Vista que maneja el formulario para agregar un nuevo Medico.
    Parecido a 'agregar_paciente': si es POST, validamos y guardamos; si no, mostramos el formulario vacío.
    """
    if request.method == 'POST':
        # Carga el formulario con los datos enviados en la request.
        form = MedicoForm(request.POST)
        if form.is_valid():
            # Guarda el médico si la validación pasa.
            form.save()
            # Redirigimos a la misma URL para limpiar el formulario
            return redirect('agregar_medico')
    else:
        # Si no es POST, mostramos un formulario vacío de MedicoForm.
        form = MedicoForm()
    return render(request, 'AppConsulta/agregar_medico.html', {'form': form})


#    VISTA: agregar_consulta

def agregar_consulta(request):
    """
    Vista para agregar una nueva Consulta.
    Maneja la fecha con validación de zona horaria.
    """
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            # Crea la instancia de consulta sin guardarla aún
            consulta = form.save(commit=False)
            # Obtén y procesa la fecha de consulta
            fecha_consulta = form.cleaned_data['fecha_consulta']
            # Asegúrate de que la fecha sea "aware"
            if is_naive(fecha_consulta):
                tz = timezone('America/Santiago')  # Zona horaria de Santiago
                fecha_consulta = make_aware(fecha_consulta, timezone=tz)
            # Asigna la fecha procesada a la instancia
            consulta.fecha_consulta = fecha_consulta
            # Guarda la consulta en la base de datos
            consulta.save()
            # Redirige a la misma página después de guardar
            return redirect('agregar_consulta')
    else:
        # Si el método no es POST, muestra un formulario vacío
        form = ConsultaForm()
    return render(request, 'AppConsulta/agregar_consulta.html', {'form': form})
#     VISTA: buscar_consulta

def buscar_consulta(request):
    """
    Permite buscar Consultas basadas en el RUT de un Paciente.
    """
    consultas = None  # Variable donde se guardan  las consultas. Se inicializa vacía

    # Captura el RUT ingresado en la URL (ej. ?rut=11.111.111-1)
    if 'rut' in request.GET:
        rut = request.GET['rut']  # Obtengo el valor del RUT que se envió por GET.
        try:
            # Busca al Paciente con ese RUT
            paciente = Paciente.objects.get(rut=rut)
            # Filtra las Consultas de ese Paciente
            consultas = Consulta.objects.filter(paciente=paciente)
        except Paciente.DoesNotExist:
            # Si no existe, no hay consultas
            consultas = []

    return render(request, 'AppConsulta/buscar_consulta.html', {'consultas': consultas})