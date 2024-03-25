from django.db import models
from pomaray.models.employee import Employee
from pomaray.models.student import Student
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

# Create your models here.

"""
Aqui se definen clases padres para instanciar clases hijas.
"""
# dummy_student = Student.objects.filter(First_Name="John", Last_Name="Doe").first()
# dummy_teacher = Employee.objects.filter(First_Name="John", Last_Name="Doe").first()


# Qualification
class Qualification(models.Model):
    Period = models.CharField(max_length=100)
    Student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    CF = models.IntegerField(default=0)
    Teacher = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True 

