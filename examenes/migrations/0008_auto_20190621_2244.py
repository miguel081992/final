# Generated by Django 2.0.6 on 2019-06-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0007_auto_20190620_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='urgencia',
            field=models.CharField(choices=[('1', 'Baja'), ('2', 'Media'), ('3', 'Alta')], default='1', max_length=1),
        ),
    ]