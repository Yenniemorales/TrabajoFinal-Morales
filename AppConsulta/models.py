from django.db import models

# Creo clase para modelo paciente 
class Paciente(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre del paciente")  # Campo de texto para el nombre
    apellido = models.CharField(max_length=30, help_text="Apellido del paciente")  # Campo de texto para el apellido
    fecha_nacimiento = models.DateField(help_text="Fecha de nacimiento (AAAA-MM-DD)")  # Campo para la fecha de nacimiento
    email = models.EmailField(help_text="Correo electrónico del paciente")  # Campo para el email

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Creo clase para modelo medico
class Medico(models.Model):
    nombre = models.CharField(max_length=30, help_text="Nombre del médico")  # Campo de texto para el nombre
    apellido = models.CharField(max_length=30, help_text="Apellido del médico")  # Campo de texto para el apellido
    especialidad = models.CharField(max_length=30, help_text="Especialidad del médico")  # Campo de texto para la especialidad
    email = models.EmailField(help_text="Correo electrónico del médico")  # Campo para el email

    def __str__(self):
        return f"Dr./Dra. {self.nombre} {self.apellido} ({self.especialidad})"

# Creo clase para modelo consulta
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, help_text="Paciente relacionado con la consulta")  # Relación con Paciente
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, help_text="Médico relacionado con la consulta")  # Relación con Médico
    fecha_consulta = models.DateTimeField(help_text="Fecha y hora de la consulta")  # Campo para la fecha y hora de la consulta
    motivo = models.TextField(help_text="Motivo de la consulta")  # Campo para el motivo

    def __str__(self):
        return f"Consulta de {self.paciente} con {self.medico} el {self.fecha_consulta.strftime('%d/%m/%Y')}"

    # Validación personalizada para fecha_consulta
    def clean(self):
        from django.core.exceptions import ValidationError
        from datetime import datetime

        if self.fecha_consulta > datetime.now():
            raise ValidationError("La fecha de la consulta no puede ser futura.")


    def __str__(self):
        return f"Consulta de {self.paciente} con {self.medico}"

