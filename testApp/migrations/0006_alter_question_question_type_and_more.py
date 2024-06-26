# Generated by Django 4.0.1 on 2024-05-04 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('1', 's'), ('2', 'unverified'), ('3', 'unverified'), ('4', 'unverified')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='quantity_of_10_Full',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.gastanks'),
        ),
    ]
