from django import forms
from .models import Paciente, Medico, Consulta
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Creo formulario de Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente  # Asociamos este formulario al modelo Paciente
        fields = '__all__'  # Incluir todos los campos del modelo

        # Personalizo los widgets para añadir estilos de Bootstrap
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del paciente'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la edad'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
        }

# Creo formulario de Médico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico  # Asociamos este formulario al modelo Médico
        fields = '__all__'  # Incluir todos los campos del modelo

        # Personalizo los widgets para añadir estilos de Bootstrap
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del médico'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido del médico'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la especialidad'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
        }

# Formulario de Consulta
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        # Personalizo los widgets para añadir estilos de Bootstrap
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'fecha_consulta': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',  #muestra solo la fecha
            }),
            'motivo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el motivo de la consulta'
            }),
        }


# Formulario de Registro
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre de usuario'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Escribe una contraseña segura'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirma tu contraseña'}),
        }


