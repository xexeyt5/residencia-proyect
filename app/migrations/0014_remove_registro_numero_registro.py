# Generated by Django 5.0.4 on 2024-05-14 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_registro_numero_registro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='numero_registro',
        ),
    ]
