from django.db import models
from pomaray.utils.person import Person
from pomaray.utils.enums import Techniques


class Student(Person):
    Technique = models.CharField(max_length=255, choices=Techniques.choices)
    Course = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.First_Name
