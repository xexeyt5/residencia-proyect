# Generated by Django 5.0.4 on 2024-06-10 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_remove_receta_ingredientes_remove_receta_sub_recetas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetaitem',
            name='registro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.registro'),
        ),
    ]
