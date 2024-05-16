# Generated by Django 4.0.1 on 2024-05-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('V', 'verified'), ('U', 'unverified')], default='U', max_length=1),
        ),
    ]