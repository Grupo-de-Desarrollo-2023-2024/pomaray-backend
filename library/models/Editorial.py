from django.db import models



class Editorial(models.Model):
    Name = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Image = models.BinaryField()

    def __str__(self) -> str:
        return self.Name
