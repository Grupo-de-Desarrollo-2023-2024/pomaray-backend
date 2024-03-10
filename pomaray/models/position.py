from django.db import models



class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion  = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre
