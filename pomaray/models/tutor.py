from django.db import models

class Tutor(models.Model):
    Cedula = models.CharField(max_length=100)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Main_contact = models.CharField(max_length=255)
    Second_contact = models.CharField(max_length=255)
    Address = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.First_name
