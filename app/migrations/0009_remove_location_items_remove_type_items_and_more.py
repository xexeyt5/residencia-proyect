# Generated by Django 5.0.4 on 2024-04-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_registro_fecha_caducidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='items',
        ),
        migrations.RemoveField(
            model_name='type',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='Location',
            field=models.ManyToManyField(related_name='Items', to='app.location'),
        ),
        migrations.AddField(
            model_name='item',
            name='types',
            field=models.ManyToManyField(related_name='Items', to='app.type'),
        ),
    ]
