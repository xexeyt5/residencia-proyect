# Generated by Django 5.0.4 on 2024-06-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_registro_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
