from django.conf import settings
from django.db import models
from django.utils import timezone


class Carpeta(models.Model):
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    caratula = models.CharField(max_length=200)
    nro_expediente = models.PositiveIntegerField(default = None)
    año = models.PositiveSmallIntegerField(default = None)
    secretaria = models.PositiveSmallIntegerField(default = None, null=True)
    descripcion = models.TextField()
    Providencia_de_autos_firme = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.caratula
