from django.db import models
from .enums import Gender
import datetime


class Person(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Full_Name = models.CharField(max_length=200, blank=True)
    Email = models.EmailField()
    Birthdate = models.DateTimeField()
    Gender = models.CharField(max_length=255, choices=Gender.choices)
    Address = models.CharField(max_length=500)
    Photo_URL = models.CharField(max_length=4000)
    IsActive = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.Full_Name = f"{self.First_Name} {self.Last_Name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Full_Name

    class Meta:
        abstract = True

    def validate_Address(self, address):
        from .models import Address  # Importación local dentro del método

        if not isinstance(address, Address):
            raise ValueError("La dirección debe ser un objeto Address")

    # Validación para el campo First_Name
    def validate_First_Name(self, first_name):
        if not isinstance(first_name, str):
            raise ValueError("El primer nombre debe ser una cadena de texto")
        if len(first_name) < 2:
            raise ValueError("El primer nombre debe tener al menos 2 caracteres")

    # Validación para el campo Last_Name
    def validate_Last_Name(self, last_name):
        if not isinstance(last_name, str):
            raise ValueError("El apellido debe ser una cadena de texto")
        if len(last_name) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres")

    # Validación para el campo Email
    def validate_Email(self, email):
        if not isinstance(email, str):
            raise ValueError("El correo electrónico debe ser una cadena de texto")
        if "@" not in email:
            raise ValueError("El correo electrónico debe ser una dirección válida")

    # Validación para el campo Birthdate
    def validate_Birthdate(self, birthdate):
        if not isinstance(birthdate, datetime.datetime):
            raise ValueError(
                "La fecha de nacimiento debe ser un objeto de tipo datetime"
            )

    # Validación para el campo Photo_URL
    def validate_Photo_URL(self, photo_url):
        if not isinstance(photo_url, str):
            raise ValueError("La URL de la foto debe ser una cadena de texto")
        if len(photo_url) > 4000:
            raise ValueError("La URL de la foto no puede exceder los 4000 caracteres")

    # Validación para el campo IsActive
    def validate_IsActive(self, is_active):
        if not isinstance(is_active, bool):
            raise ValueError("IsActive debe ser un valor booleano")
