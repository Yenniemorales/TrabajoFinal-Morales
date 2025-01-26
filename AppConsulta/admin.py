from django.contrib import admin
from .models import Paciente, Medico, Consulta
from .models import Profile
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)


# Para las imagenes
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']
