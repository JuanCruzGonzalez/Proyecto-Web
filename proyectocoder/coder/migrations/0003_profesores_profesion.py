# Generated by Django 4.1.2 on 2022-11-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0002_entregable_estudiante_profesores'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesores',
            name='profesion',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]