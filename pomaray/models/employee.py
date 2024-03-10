from django.db import models
from pomaray.utils.models import Person
from pomaray.models.department import Department
from pomaray.models.position import Cargo



class Employee(Person):
    Departament = models.ForeignKey(Department,  on_delete=models.CASCADE, max_length=100)
    Position = models.ForeignKey(Cargo,  on_delete=models.CASCADE, max_length=100)

    def __str__(self) -> str:
        return self.First_Name
