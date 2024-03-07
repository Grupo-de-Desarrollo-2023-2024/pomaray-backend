from django.db import models

# Create your models here.
class Persona(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Birthdate = models.DateTimeField()
    Gender = models.CharField(max_length=255)
    Address = models.TextField(max_length=250)
    Photo = models.BinaryField()

    class Meta:
        abstract = True  # Indica que esta clase no se debe crear como una tabla en la base de datos

# Clase derivada que hereda de BaseFields y agrega campos adicionales
class Employee(Persona):
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)

class Student(Persona):
    Tecnica = models.CharField(max_length=255)
    Curso = models.CharField(max_length=255)