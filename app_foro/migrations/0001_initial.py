# Generated by Django 4.0.4 on 2022-05-27 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('tema_especifico', models.CharField(max_length=50)),
                ('consulta', models.TextField()),
                ('fecha_de_consuta', models.DateField(default=datetime.datetime(2022, 5, 27, 18, 11, 26, 430064))),
            ],
        ),
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('razon_contacto', models.TextField()),
                ('fecha_de_contacto', models.DateField(default=datetime.datetime(2022, 5, 27, 18, 11, 26, 471101))),
            ],
        ),
        migrations.CreateModel(
            name='sorteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
