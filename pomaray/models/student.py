from django.db import models
from pomaray.utils.models import Persona


class Student(Persona):
    Tecnica = models.CharField(max_length=255)
    Curso = models.CharField(max_length=255)
