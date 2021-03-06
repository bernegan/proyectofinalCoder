# Generated by Django 4.0.4 on 2022-06-10 02:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_foro', '0005_alter_contacto_fecha_de_contacto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha_de_contacto',
            field=models.DateField(default=datetime.datetime(2022, 6, 9, 23, 30, 3, 431118)),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_de_publicacion',
            field=models.DateField(default=datetime.datetime(2022, 6, 9, 23, 30, 3, 431118)),
        ),
        migrations.CreateModel(
            name='avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
