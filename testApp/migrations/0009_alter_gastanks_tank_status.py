# Generated by Django 4.0.1 on 2024-05-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0008_pricetanks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastanks',
            name='tank_status',
            field=models.CharField(choices=[('Full', 'Full'), ('Empty', 'Empty')], default='Full', max_length=5),
        ),
    ]
