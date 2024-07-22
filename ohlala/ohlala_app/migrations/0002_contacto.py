# Generated by Django 5.0.7 on 2024-07-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohlala_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idContacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('correo_electronico', models.CharField(max_length=45, unique=True)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
