from django.db import models
from pomaray.models.student import Student
from library.models.Book import Book

class Loan(models.Model):
    Student = models.ForeignKey(Student ,on_delete=models.CASCADE, max_length=100)
    Loan_Date = models.DateField()
    Book = models.ForeignKey(Book ,on_delete=models.CASCADE, max_length=100)
    Return_Date = models.DateField()
    In_Use = models.BooleanField()

    def __str__(self) -> str:
        return 'Tomado por ' + self.Student.First_Name + ' el ' + self.Loan_Date.strftime("%m/%d/%Y")
