# Generated by Django 3.0.2 on 2020-02-07 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0010_tubelight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tubelight',
            name='a_flux',
        ),
    ]
