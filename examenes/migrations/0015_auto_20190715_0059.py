# Generated by Django 2.0.6 on 2019-07-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0014_auto_20190710_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='descripcion_examen',
            field=models.TextField(default='No hay descripción', max_length=1000),
        ),
    ]
