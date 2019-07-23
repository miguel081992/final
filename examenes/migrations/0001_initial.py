# Generated by Django 2.0.6 on 2019-06-12 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_cat', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id_cita', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id_examen', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_examen', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examenes.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_paciente', models.CharField(max_length=50)),
                ('apellidos_paciente', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
