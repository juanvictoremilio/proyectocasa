from django.db import models

# Create your models here.

class Material(models.Model):
    fecha = models.DateField()
    concepto = models.CharField(max_length=120)
    proveedor = models.CharField(max_length=120)
    cantidad = models.DecimalField(decimal_places=2, max_digits=8)


    def __str__(self):
        return self.concepto

    class Meta:
        
        verbose_name_plural = "Material"   



class Servicios(models.Model):
    fecha = models.DateField()
    concepto = models.CharField(max_length=120)
    proveedor = models.CharField(max_length=120)
    cantidad = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.concepto

    class Meta:
        verbose_name_plural = "Pago de Servicios"   
