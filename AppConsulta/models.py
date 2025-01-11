from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

# Modelo para la clase Paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre del paciente")  # Nombre del paciente
    apellido = models.CharField(max_length=30, help_text="Apellido del paciente")  # Apellido del paciente
    fecha_nacimiento = models.DateField(help_text="Fecha de nacimiento (AAAA-MM-DD)")  # Fecha de nacimiento
    email = models.EmailField(help_text="Correo electrónico del paciente")  # Email del paciente

    def __str__(self):
        # Retorna una representación amigable del paciente
        return f"{self.nombre} {self.apellido}"


# Modelo para la clase Médico
class Medico(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre del médico")  # Nombre del médico
    apellido = models.CharField(max_length=30, help_text="Apellido del médico")  # Apellido del médico
    especialidad = models.CharField(max_length=30, help_text="Especialidad del médico")  # Especialidad
    email = models.EmailField(help_text="Correo electrónico del médico")  # Email del médico

    def __str__(self):
        # Retorna una representación amigable del médico
        return f"Dr./Dra. {self.nombre} {self.apellido} ({self.especialidad})"


# Modelo para la clase Consulta
class Consulta(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        help_text="Paciente relacionado con la consulta"
    )  # Relación con el modelo Paciente
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        help_text="Médico relacionado con la consulta"
    )  # Relación con el modelo Médico
    fecha_consulta = models.DateTimeField(
        help_text="Fecha y hora de la consulta"
    )  # Fecha y hora de la consulta
    motivo = models.TextField(help_text="Motivo de la consulta")  # Motivo de la consulta

    def clean(self):
        """
        Validación personalizada para asegurarse de que la fecha de la consulta
        no esté en el futuro.
        """
        # Verifica que la fecha de consulta no sea nula
        if self.fecha_consulta and self.fecha_consulta > datetime.now():
            # Lanza un error si la fecha es futura
            raise ValidationError("La fecha de la consulta no puede ser futura.")

    def __str__(self):
        # Representación amigable de la consulta
        return f"Consulta de {self.paciente} con {self.medico} el {self.fecha_consulta.strftime('%d/%m/%Y')}"
