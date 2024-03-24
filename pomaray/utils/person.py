from django.db import models
from .enums import Gender

class Person(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Full_Name = models.CharField(max_length=200, blank=True)
    Email = models.EmailField()
    Birthdate = models.DateTimeField()
    Gender = models.CharField(max_length=255, choices=Gender.choices)
    Address = models.TextField(max_length=250)
    Photo_URL = models.CharField(max_length=4000)
    IsActive = models.BooleanField(default=True)  
    def save(self, *args, **kwargs):
        self.Full_Name = f"{self.First_Name} {self.Last_Name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Full_Name

    class Meta:
        abstract = True
