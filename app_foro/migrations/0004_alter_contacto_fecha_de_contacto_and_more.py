# Generated by Django 4.0.4 on 2022-05-31 04:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foro', '0003_remove_publicacion_fecha_de_consuta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha_de_contacto',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 1, 10, 15, 325451)),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_de_publicacion',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 1, 10, 15, 284413)),
        ),
    ]
