# Generated by Django 3.0.2 on 2020-02-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0006_auto_20200204_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='usage',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
