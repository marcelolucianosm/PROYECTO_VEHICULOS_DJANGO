# Generated by Django 5.1.2 on 2024-10-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('chevrolet', 'Chevrolet'), ('fiat', 'Fiat'), ('ford', 'Ford'), ('toyota', 'Toyota')], default='Ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('particular', 'Particular'), ('transporte', 'Transporte'), ('carga', 'Carga')], default='Particular', max_length=20)),
                ('precio', models.PositiveIntegerField(max_length=999999999)),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_modificacion', models.DateTimeField()),
            ],
        ),
    ]