# Generated by Django 2.1.2 on 2018-11-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0005_auto_20181031_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_perfil'),
        ),
    ]
