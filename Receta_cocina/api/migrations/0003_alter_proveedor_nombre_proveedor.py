# Generated by Django 5.1.2 on 2024-10-24 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_ingredientes_nombre_ingrediente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='Nombre_Proveedor',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
