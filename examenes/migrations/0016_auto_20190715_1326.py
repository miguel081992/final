# Generated by Django 2.0.6 on 2019-07-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0015_auto_20190715_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resexamen',
            name='ResultadosExamen',
            field=models.TextField(max_length=2000),
        ),
    ]
