from django.db import models
from library.models.Author import Author
from library.models.Editorial import Editorial





class Book(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Author = models.ForeignKey(Author,on_delete=models.CASCADE, max_length=100)
    Editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE, max_length=100)
    Gender = models.CharField(max_length=100)
    Release_date = models.DateField(max_length=100)
    Available = models.BooleanField()
    Image = models.BinaryField()

    def __str__(self) -> str:
        return self.Name
