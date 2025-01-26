from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.timezone import make_aware
from django.contrib.auth.models import User

# Modelo para la clase Paciente
class Paciente(models.Model):
    # Los campos nombre, apellido, rut, fecha_nacimiento y email son obligatorios
    nombre = models.CharField(max_length=30, help_text="Nombre del paciente")
    apellido = models.CharField(max_length=30, help_text="Apellido del paciente")
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField(help_text="Fecha de nacimiento (AAAA-MM-DD)")
    email = models.EmailField(help_text="Correo electrónico del paciente")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"

# Modelo para la clase Médico
class Medico(models.Model):
    # Los campos nombre, apellido, rut, especialidad y email son obligatorios
    nombre = models.CharField(max_length=30, help_text="Nombre del médico")
    apellido = models.CharField(max_length=30, help_text="Apellido del médico")
    rut = models.CharField(max_length=12, unique=True)
    especialidad = models.CharField(max_length=30, help_text="Especialidad del médico")
    email = models.EmailField(help_text="Correo electrónico del médico")

    def __str__(self):
        return f"Dr./Dra. {self.nombre} {self.apellido} ({self.especialidad}) - {self.rut}"

# Modelo para la clase Consulta
class Consulta(models.Model):
    # El campo paciente se relaciona con la clase Paciente
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        help_text="Paciente relacionado con la consulta"
    )

    # El campo medico se relaciona con la clase Medico
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        help_text="Médico relacionado con la consulta"
    )
    # El campo fecha_consulta lo que hace es almacenar la fecha y hora de la consulta
    fecha_consulta = models.DateTimeField(help_text="Fecha y hora de la consulta")
    motivo = models.TextField(help_text="Motivo de la consulta")

# Validación personalizada para la fecha de la consulta
    def clean(self):
        if self.fecha_consulta:
            fecha_consulta_aware = (
                self.fecha_consulta
                if timezone.is_aware(self.fecha_consulta)
                else make_aware(self.fecha_consulta)
            )
            # Verificar si la fecha de la consulta es futura
            if fecha_consulta_aware > timezone.now():
                raise ValidationError("La fecha de la consulta no puede ser futura.")

    def __str__(self):
        return f"Consulta de {self.paciente} con {self.medico} el {self.fecha_consulta.strftime('%d/%m/%Y')}"

# Imagen 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/ozzy.png')

    def __str__(self):
        return f"Perfil de {self.user.username}"
