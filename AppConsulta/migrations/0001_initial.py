# Generated by Django 5.1.5 on 2025-01-25 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del médico', max_length=30)),
                ('apellido', models.CharField(help_text='Apellido del médico', max_length=30)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('especialidad', models.CharField(help_text='Especialidad del médico', max_length=30)),
                ('email', models.EmailField(help_text='Correo electrónico del médico', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del paciente', max_length=30)),
                ('apellido', models.CharField(help_text='Apellido del paciente', max_length=30)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('fecha_nacimiento', models.DateField(help_text='Fecha de nacimiento (AAAA-MM-DD)')),
                ('email', models.EmailField(help_text='Correo electrónico del paciente', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_consulta', models.DateTimeField(help_text='Fecha y hora de la consulta')),
                ('motivo', models.TextField(help_text='Motivo de la consulta')),
                ('medico', models.ForeignKey(help_text='Médico relacionado con la consulta', on_delete=django.db.models.deletion.CASCADE, to='AppConsulta.medico')),
                ('paciente', models.ForeignKey(help_text='Paciente relacionado con la consulta', on_delete=django.db.models.deletion.CASCADE, to='AppConsulta.paciente')),
            ],
        ),
    ]
