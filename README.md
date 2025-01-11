# Gestión de Consultas Médicas

Proyecto simple desarrollado con **Django** y **Bootstrap** para gestionar pacientes, médicos y consultas médicas.

---

## Características Principales

- **Registro de pacientes** con datos como nombre, apellido, RUT y fecha de nacimiento.
- **Gestión de médicos**, incluyendo su especialidad.
- **Agendamiento de consultas** asociando pacientes y médicos.
- **Búsqueda de consultas** por RUT del paciente.

---

## Instalación y Configuración

### 1. Clonar el repositorio
Se clona el repositorio y navega al directorio del proyecto:
```bash
git clone https://github.com/Yenniemorales/TuPrimeraPagina-Morales.git
cd TuPrimeraPagina-Morales
```

### 2. Creación el entorno virtual y activarlo
Creación de un entorno virtual para instalar las dependencias necesarias y actívalo:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Realización de las migraciones y ejecutar el servidor
Se configura la base de datos realizando las migraciones y ejecuta el servidor para iniciar la aplicación:
```bash
python manage.py migrate
python manage.py runserver
```
---

## Pasos para Construir la Página

### 1. Creación de Modelos
Definimos tres modelos principales en `models.py`:
```python
class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()

class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
    especialidad = models.CharField(max_length=30)

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateField()
    motivo = models.TextField()
```

### 2. Creación de Formularios
Los formularios para capturar datos de pacientes, médicos y consultas se definieron en `forms.py` usando `ModelForm`.

### 3. Vistas
Se implementaron vistas en `views.py` para manejar las funcionalidades:
```python
def home(request):
    total_pacientes = Paciente.objects.count()
    total_medicos = Medico.objects.count()
    total_consultas = Consulta.objects.count()
    registros_recientes = [...]
    return render(request, 'home.html', {'registros_recientes': registros_recientes})

def buscar_consulta(request):
    if 'rut' in request.GET:
        consultas = Consulta.objects.filter(paciente__rut=request.GET['rut'])
        return render(request, 'buscar_consulta.html', {'consultas': consultas})
    return render(request, 'buscar_consulta.html')
```

### 4. Plantillas (Templates)
Se usaron plantillas HTML con Bootstrap para diseñar la interfaz. Ejemplo de la barra de navegación:
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <a class="navbar-brand" href="{% url 'home' %}">Consulta Médica</a>
</nav>
```

### 5. Configuración del Proyecto
Después de definir los modelos y vistas:
1. Realizamos las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Ejecutamos el servidor local:
   ```bash
   python manage.py runserver
   ```

---

## Autor
Creado por **[Yennie Morales](https://github.com/Yenniemorales)**

---

Este proyecto está disponible en [GitHub](https://github.com/Yenniemorales/TuPrimeraPagina-Morales).


