# Generated by Django 2.0.6 on 2018-06-27 01:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20180626_2155'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Puntajes',
            new_name='Puntaje',
        ),
    ]
