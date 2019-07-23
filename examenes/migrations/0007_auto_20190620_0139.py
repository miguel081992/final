# Generated by Django 2.0.6 on 2019-06-20 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examenes', '0006_delete_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicacion',
            fields=[
                ('id_indicacion', models.AutoField(primary_key=True, serialize=False)),
                ('num_indicacion', models.IntegerField()),
                ('contenido', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'indicacion',
                'verbose_name_plural': 'indicaciones',
                'db_table': 'TblIndicaciones',
                'ordering': ['id_indicacion'],
            },
        ),
        migrations.CreateModel(
            name='ResExamen',
            fields=[
                ('id_resExamen', models.AutoField(primary_key=True, serialize=False)),
                ('ResultadosExamen', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'resultado de examen',
                'verbose_name_plural': 'resultados de examenes',
                'db_table': 'TblResExamen',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_medico', models.CharField(max_length=200)),
                ('institucion_solicitante', models.CharField(max_length=100)),
                ('diagnostico_presuntivo', models.TextField(max_length=2000)),
                ('fecha_solicitud', models.DateField(auto_now=True)),
                ('urgencia', models.CharField(choices=[('1', 'Baja'), ('2', 'Media'), ('2', 'Alta')], default='1', max_length=1)),
                ('estado_solicitud', models.CharField(choices=[('1', 'Registrada'), ('2', 'En Proceso'), ('3', 'Cancelada'), ('4', 'Completada'), ('5', 'Parcialmente Completada')], default='1', max_length=1)),
                ('notas_solicitud', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'solicitud',
                'verbose_name_plural': 'solicitudes',
                'db_table': 'TblSolicitudes',
                'ordering': ['fecha_solicitud'],
            },
        ),
        migrations.RemoveField(
            model_name='cita',
            name='paciente',
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='examen',
            options={'ordering': ['nombre_examen'], 'verbose_name': 'examen', 'verbose_name_plural': 'examenes'},
        ),
        migrations.AlterModelOptions(
            name='horario',
            options={'ordering': ['fecha_actualizacion'], 'verbose_name': 'horario', 'verbose_name_plural': 'horarios'},
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre_cat',
            new_name='nombre_categoria',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='id',
            new_name='id_horario',
        ),
        migrations.AddField(
            model_name='examen',
            name='descripcion_examen',
            field=models.TextField(default='no hay descripcion', max_length=1000),
        ),
        migrations.AddField(
            model_name='horario',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='fecha_presentacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='hora_presentacion',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='categoria',
            table='TblCategoria',
        ),
        migrations.AlterModelTable(
            name='examen',
            table='TblExamenes',
        ),
        migrations.AlterModelTable(
            name='horario',
            table='TblHorario',
        ),
        migrations.DeleteModel(
            name='Cita',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='categoria',
            field=models.ManyToManyField(to='examenes.Categoria'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='examen',
            field=models.ManyToManyField(to='examenes.Examen'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resexamen',
            name='ExamenSeleccionado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examenes.Solicitud'),
        ),
        migrations.AddField(
            model_name='indicacion',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examenes.Categoria'),
        ),
        migrations.AddField(
            model_name='horario',
            name='solicitud_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='examenes.Solicitud'),
        ),
    ]
