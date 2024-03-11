from django.db import models
from pomaray.utils.person import Person
from pomaray.utils.enums import Techniques, Course



class Student(Person):
    Technique = models.CharField(max_length=255, choices=Techniques.choices)
    Course = models.CharField(max_length=255, choices=Course.choices)

    def __str__(self) -> str:
        return self.First_Name
