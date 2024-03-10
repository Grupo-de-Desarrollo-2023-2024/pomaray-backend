from django.db import models
from pomaray.utils.models import Person


class Student(Person):
    Technique = models.CharField(max_length=255)
    Course = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.First_Name
