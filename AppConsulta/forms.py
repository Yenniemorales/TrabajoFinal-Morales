from django import forms
from .models import Paciente, Medico, Consulta

#Creo formulario de Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        #Llamo todos los campos
        fields = '__all__'

#Creo formulario de Medico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        #Llamo todos los campos
        fields = '__all__'

#Creo formulario de Consulta
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        #Llamo todos los campos
        fields = '__all__'
