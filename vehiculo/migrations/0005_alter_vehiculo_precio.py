# Generated by Django 5.1.2 on 2024-11-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_alter_vehiculo_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='precio',
            field=models.FloatField(),
        ),
    ]