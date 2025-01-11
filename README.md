 Gestión de Consultas Médicas

Aplicación web para gestionar pacientes, médicos y consultas médicas, desarrollada con **Django** y **Bootstrap**.

---

## Características Principales

1. **Registro y gestión de pacientes**:
   - Captura de datos como nombre, apellido, RUT y fecha de nacimiento.
2. **Gestión de médicos**:
   - Registro de médicos con sus datos personales y especialidad.
3. **Gestión de consultas**:
   - Agendar consultas médicas asociando pacientes y médicos.
   - Búsqueda de consultas por RUT del paciente.
4. **Interfaz adaptable**:
   - La interfaz está diseñada con **Bootstrap** para adaptarse a cualquier dispositivo.

---

## Instalación y Configuración

### 1. Clonar el repositorio
Clona el repositorio en tu máquina local y navega al directorio del proyecto:
```bash
git clone https://github.com/Yenniemorales/TuPrimeraPagina-Morales.git
cd TuPrimeraPagina-Morales
```

### 2. Crear el entorno virtual y activarlo
Crea un entorno virtual para instalar las dependencias necesarias y actívalo:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Realizar las migraciones y ejecutar el servidor
Configura la base de datos realizando las migraciones y ejecuta el servidor para iniciar la aplicación:
```bash
python manage.py migrate
python manage.py runserver
```

Abre tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000) para acceder a la aplicación.

---

## Construcción del Proyecto

### Modelos
Los modelos principales del proyecto son:

#### **Paciente**
```python
class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
```

#### **Médico**
```python
class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
    especialidad = models.CharField(max_length=30)
```

#### **Consulta**
```python
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateField()
    motivo = models.TextField()
```

---

## Código Destacado

### **Vista: Buscar Consulta**
```python
def buscar_consulta(request):
    if 'rut' in request.GET:
        consultas = Consulta.objects.filter(paciente__rut=request.GET['rut'])
        return render(request, 'buscar_consulta.html', {'consultas': consultas})
    return render(request, 'buscar_consulta.html')
```

---

## Autor

Creado por **[Yennie Morales](https://github.com/Yenniemorales)**

