from django.db import models
from pomaray.utils.models import Person
from pomaray.models.department import Department


class Employee(Person):
    Departamento = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.First_Name
