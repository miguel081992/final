# Generated by Django 2.0.6 on 2019-07-11 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0013_auto_20190623_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='estado_solicitud',
            field=models.CharField(choices=[('1', 'Registrada'), ('2', 'En Proceso'), ('3', 'Cancelada'), ('4', 'Completada'), ('5', 'Parcialmente')], default='1', max_length=1),
        ),
    ]
