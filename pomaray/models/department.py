from django.db import models



class Department(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre
