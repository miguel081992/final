# Generated by Django 2.0.6 on 2019-06-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0008_auto_20190621_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='notas_solicitud',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]