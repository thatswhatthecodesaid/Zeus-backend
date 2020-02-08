# Generated by Django 3.0.2 on 2020-02-07 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200208_0023'),
        ('iot', '0009_lockout'),
    ]

    operations = [
        migrations.CreateModel(
            name='tubeLight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_flux', models.CharField(max_length=100)),
                ('a_io', models.BooleanField()),
                ('a_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Appliances')),
            ],
        ),
    ]
