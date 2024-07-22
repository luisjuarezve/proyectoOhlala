from django.db import models
from account_manager.models import Cliente
# Create your models here.


class Manicurista(models.Model):
    idManicurista = models.AutoField(primary_key=True)
    cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return self.correo_electronico


class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    precio = models.FloatField()

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    idCita = models.AutoField(primary_key=True)
    fechaCita = models.DateField()
    horaCita = models.TimeField()
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idManicurista = models.ForeignKey(Manicurista, on_delete=models.CASCADE)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cita {self.idCita} para {self.idCliente}"


class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    correo_electronico = models.CharField(max_length=45, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"Cita {self.idContacto} para {self.correo_electronico}"
