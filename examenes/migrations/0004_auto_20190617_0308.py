# Generated by Django 2.0.6 on 2019-06-17 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0003_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
