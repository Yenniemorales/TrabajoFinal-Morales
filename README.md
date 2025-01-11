# Gestión de Consultas Médicas

Este proyecto es una aplicación web diseñada para gestionar pacientes, médicos y consultas médicas. Fue desarrollada utilizando **Django** como framework principal y **Bootstrap** para la interfaz de usuario.

---

## Características Principales

1. **Registro y gestión de pacientes**:
   - Captura de datos como nombre, apellido, RUT y fecha de nacimiento.

2. **Gestión de médicos**:
   - Registro de médicos con sus datos personales y especialidad.

3. **Gestión de consultas**:
   - Agendar consultas médicas asociando pacientes y médicos.
   - Búsqueda de consultas por RUT del paciente.

4. **Interfaz**:
   - La interfaz está diseñada con **Bootstrap** para adaptarse a cualquier dispositivo.

---

## Instalación y Configuración

### 1. Clona el repositorio
Clona el repositorio en tu máquina local y navega al directorio del proyecto:

```bash
git clone https://github.com/Yenniemorales/TuPrimeraPagina-Morales.git
cd TuPrimeraPagina-Morales
2. Crea el entorno virtual y actívalo
Crea un entorno virtual para instalar las dependencias necesarias y actívalo:

bash
Copiar código
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
3. Realiza las migraciones y ejecuta el servidor
Configura la base de datos realizando las migraciones y ejecuta el servidor para iniciar la aplicación:

bash
Copiar código
python manage.py migrate
python manage.py runserver
Abre tu navegador en http://127.0.0.1:8000 para acceder a la aplicación.

Construcción del Proyecto
Modelos
Los modelos principales del proyecto son:

Paciente
python
Copiar código
class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
Médico
python
Copiar código
class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
Consulta
python
Copiar código
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateField()
    motivo = models.TextField()
Formularios
Se utilizaron formularios en Django para capturar los datos necesarios:

python
Copiar código
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
Vistas
Algunas de las vistas principales incluyen:

Agregar Paciente
python
Copiar código
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PacienteForm()
    return render(request, 'AppConsulta/agregar_paciente.html', {'form': form})
Buscar Consulta por RUT
python
Copiar código
def buscar_consulta(request):
    if 'rut' in request.GET:
        rut = request.GET['rut']
        consultas = Consulta.objects.filter(paciente__rut=rut)
        return render(request, 'AppConsulta/buscar_consulta.html', {'consultas': consultas})
    return render(request, 'AppConsulta/buscar_consulta.html')
Plantillas
Las plantillas están diseñadas con Bootstrap. Ejemplo de la barra de navegación:

html
Copiar código
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
        <a class="navbar-brand fs-4 fw-bold" href="{% url 'home' %}">Consulta Médica</a>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'agregar_paciente' %}">Agregar Paciente</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
Capturas de Pantalla
Inicio

Agregar Paciente

Buscar Consulta

Licencia
Este proyecto está licenciado bajo la MIT License.

Autor
Yennie Morales

less
Copiar código


