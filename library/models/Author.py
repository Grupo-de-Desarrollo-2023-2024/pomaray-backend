from django.db import models



class Author(models.Model):
    Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Image = models.BinaryField()

    def __str__(self) -> str:
        return self.Name
