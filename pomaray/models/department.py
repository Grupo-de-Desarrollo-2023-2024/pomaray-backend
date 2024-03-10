from django.db import models



class Department(models.Model):
    Name = models.CharField(max_length=100)
    Description  = models.CharField(max_length=100)
    Status = models.BooleanField()

    def __str__(self) -> str:
        return self.nombre
