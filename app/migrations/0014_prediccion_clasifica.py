# Generated by Django 2.0.6 on 2018-06-29 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_partido_prediccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediccion',
            name='clasifica',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
