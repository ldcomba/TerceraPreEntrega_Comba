from django.db import models

# Create your models here.
class Impresora(models.Model):
    fabricante=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    diametroFilamento=models.DecimalField(max_digits=10,decimal_places=2)
    fechaDeCompra=models.DateField()
    precioArs=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f" {self.fabricante} - {self.modelo}"


class RolloFilamento(models.Model):
    fabricante=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    material=models.CharField(max_length=50)
    fechaDeCompra=models.DateField()
    precioArs=models.DecimalField(max_digits=10,decimal_places=2)
    dimetroFilamento=models.DecimalField(max_digits=10,decimal_places=2)
    pesoGramos=models.DecimalField(max_digits=10, decimal_places=2)
    disponible=models.BooleanField()
    def __str__(self):
        return f" {self.fabricante} - {self.color} - {self.pesoGramos} - {self.disponible}"

class Archivo3mf(models.Model):
    nombreArchivo=models.CharField(max_length=50)
    fechaCreacion=models.DateField()
    material=models.CharField(max_length=50)
    tiempoImpresion=models.TimeField()
    pesoGramos=models.DecimalField(max_digits=10, decimal_places=2)
    impresora=models.CharField(max_length=50)
    def __str__(self):
        return f" {self.nombreArchivo} - {self.fechaCreacion} - {self.material} - {self.tiempoImpresion} - {self.pesoGramos} - {self.impresora}"
        
