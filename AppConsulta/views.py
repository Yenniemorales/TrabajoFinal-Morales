from django.shortcuts import render, redirect
from .forms import PacienteForm, MedicoForm, ConsultaForm
from .models import Consulta
from django.http import HttpResponse
from django.shortcuts import render
#Creo vista para home(inicio)

def home(request):
    return render(request, 'AppConsulta/base.html')  # Redirige a la base.html para pruebas iniciales


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
def agregar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_consulta')
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
