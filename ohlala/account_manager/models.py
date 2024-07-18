from django.db import models

# Create your models here.


class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cuenta(models.Model):
    idCliente = models.OneToOneField(
        Cliente, on_delete=models.CASCADE, primary_key=True)
    correo_electronico = models.CharField(max_length=45, unique=True)
    contrasena = models.CharField(max_length=45)
