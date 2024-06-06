# Generated by Django 4.0.1 on 2024-06-06 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0012_alter_gastanks_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='gastanks',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='testApp.warehouse'),
        ),
        migrations.AlterField(
            model_name='pricetanks',
            name='tank_type',
            field=models.CharField(blank=True, choices=[('10', '10'), ('13', '13'), ('25', '25'), ('0', '0')], max_length=2),
        ),
    ]