# Generated by Django 2.0.6 on 2018-06-29 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180628_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puntaje',
            name='puntos',
        ),
    ]
