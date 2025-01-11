from django import forms
from .models import Paciente, Medico, Consulta

# Creo formulario de Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente  # Asociamos este formulario al modelo Paciente
        fields = '__all__'  # Incluir todos los campos del modelo

        # Perzonalizo los widgets para añadir estilos de Bootstrap
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del paciente'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la edad'}),
        }

# Creo formulario de Medico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico  # Asociamos este formulario al modelo Medico
        fields = '__all__'  # Incluir todos los campos del modelo

        # Perzonalizo los widgets para añadir estilos de Bootstrap
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del médico'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la especialidad'}),
        }

# Creo formulario de Consulta
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta  # Asociamos este formulario al modelo Consulta
        fields = '__all__'  # Incluir todos los campos del modelo

        # Perzonalizo los widgets para añadir estilos de Bootstrap
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el motivo de la consulta'}),
        }
