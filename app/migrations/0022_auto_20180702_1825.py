# Generated by Django 2.0.6 on 2018-07-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20180702_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='fase_eliminatoria',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]