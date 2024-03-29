from django.db import models
from pomaray.utils.person import Person
from pomaray.models.department import Department
from pomaray.models.position import Cargo
from pomaray.utils.enums import Departments, Positions



class Employee(Person):
    Departament = models.CharField(max_length=100, choices=Departments.choices)
    Position = models.CharField(max_length=100, choices=Positions.choices)

    def __str__(self) -> str:
        return self.First_Name
