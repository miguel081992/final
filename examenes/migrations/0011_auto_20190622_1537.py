# Generated by Django 2.0.6 on 2019-06-22 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0010_remove_solicitud_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examen',
            options={'ordering': ['categoria'], 'verbose_name': 'examen', 'verbose_name_plural': 'examenes'},
        ),
    ]
