from django.db import models

from pomaray.models.student import Student
from pomaray.models.tutor import Tutor

class Emergency(models.Model):
    medical_information = models.TextField(max_length=250)
    Student = models.ForeignKey(Student,  on_delete=models.CASCADE, max_length=100)
    Tutor = models.ForeignKey(Tutor,  on_delete=models.CASCADE, max_length=100)

    def __str__(self) -> str:
        return f"Emergency - Student: {self.Student}, Tutor: {self.Tutor}"