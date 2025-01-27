# Gestión de Consultas Médicas

Proyecto simple desarrollado con **Django** y **Bootstrap** para gestionar pacientes, médicos y consultas médicas.

---

## Características Principales

- **Registro de pacientes** con datos como nombre, apellido, RUT y fecha de nacimiento.
- **Gestión de médicos**, incluyendo su especialidad.
- **Agendar consultas** asociando pacientes y médicos.
- **Creación CRUD** para pacientes, médicos y consultas médicas.
- **Registro y autenticación de usuarios**.
- **Creación y actualización de avatar** personalizado.
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
Definimos cuatro modelos principales en `models.py`:
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/ozzy.png')

urn f"Perfil de {self.user.username}"

```

### 2. Vistas
Se implementaron vistas en `views.py` para manejar las funcionalidades:
```python
@login_required
def home(request):
    total_pacientes = Paciente.objects.count()
    total_medicos = Medico.objects.count()
    total_consultas = Consulta.objects.count()

    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    consultas = Consulta.objects.all()

def buscar_consulta(request):
    if 'rut' in request.GET:
        consultas = Consulta.objects.filter(paciente__rut=request.GET['rut'])
        return render(request, 'buscar_consulta.html', {'consultas': consultas})
    return render(request, 'buscar_consulta.html')
```
### 3. Registro y Login de Usuarios
Se implementó un sistema de registro y autenticación usando las herramientas de Django:
```python
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user

# Vista para registro de usuario
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
```

### 4. Creación y Edición de Avatar
Los usuarios pueden subir o actualizar su avatar desde un formulario personalizado:

```python
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

# Vista para editar perfil
def editar_perfil(request):
    usuario = request.user
    perfil, created = Profile.objects.get_or_create(user=usuario)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=usuario)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('home')
    else:
        user_form = UserEditForm(instance=usuario)
        profile_form = ProfileEditForm(instance=perfil)

    return render(request, 'editar_perfil.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
```

### 5. Plantillas (Templates)
Se usaron plantillas HTML con Bootstrap para diseñar la interfaz. Ejemplo de barra de navegación:
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <a class="navbar-brand" href="{% url 'home' %}">Consulta Médica</a>
</nav>
```

---

## Autor
Creado por **[Yennie Morales](https://github.com/Yenniemorales)**

---

Este proyecto está disponible en [GitHub](https://github.com/Yenniemorales/TrabajoFinal-Morales).

