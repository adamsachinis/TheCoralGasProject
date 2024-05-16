# Generated by Django 4.0.1 on 2024-05-03 18:21

from django.db import migrations, models
import testApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_gastanks_tank_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_of_10_Full', models.PositiveIntegerField(verbose_name=testApp.models.GasTanks)),
                ('quantity_of_13_Full', models.PositiveIntegerField(verbose_name=testApp.models.GasTanks)),
                ('quantity_of_13_Empty', models.PositiveIntegerField(verbose_name=testApp.models.GasTanks)),
            ],
        ),
    ]
