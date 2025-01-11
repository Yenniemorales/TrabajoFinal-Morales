from django.db import models

# Create your models here.
from django.db import models

# Creo clase para modelo paciente 
class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"Nombre:{self.nombre} Apellido:{self.apellido}"

# Creo clase para modelo medico
class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre:{self.nombre} Apellido:{self.apellido} Especialidad:{self.especialidad}"

# Creo clase para modelo consulta
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Consulta de {self.paciente} con {self.medico}"

