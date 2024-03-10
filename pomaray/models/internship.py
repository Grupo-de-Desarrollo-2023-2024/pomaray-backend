from django.db import models
from pomaray.models.student import Student
from pomaray.models.employee import Employee



class Internship(models.Model):
    Company_Name = models.CharField(max_length=100)
    Description  = models.CharField(max_length=100)
    Description  = models.CharField(max_length=100)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE, max_length=100)
    Supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE, max_length=100)
    Start_Date = models.DateField()
    End_Date = models.DateField(blank=True)
    Evaluation = models.CharField(max_length=100)
    Hours_so_far = models.IntegerField()
    Hours_to_complete = models.IntegerField()
    Status = models.BooleanField()

    def __str__(self) -> str:
        return self.Company_Name
