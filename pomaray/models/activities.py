from django.db import models



class Activities(models.Model):
    Name = models.CharField(max_length=100)
    Place  = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Name
