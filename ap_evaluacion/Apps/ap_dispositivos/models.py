from django.db import models

# Create your models here.


class AP_Dispositivos(models.Model):
    ap_nombre = models.CharField(max_length=100, help_text="Ingrese el Nombre")
    ap_marca = models.CharField(max_length=100, help_text="Ingrese la Marca")
    ap_precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    ap_descripcion = models.CharField(max_length=100, help_text="Ingrese una Descripcion")

    class Meta:
        verbose_name = "ap_dispositivo"
        verbose_name_plural = "ap_dispositivos"