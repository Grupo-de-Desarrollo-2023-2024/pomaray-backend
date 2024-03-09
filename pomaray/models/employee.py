from django.db import models
from utils.models import Persona


class Employee(Persona):
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
