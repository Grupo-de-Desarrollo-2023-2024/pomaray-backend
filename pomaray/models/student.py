from django.db import models
from pomaray.utils.person import Person
from pomaray.utils.enums import Techniques, Course
from datetime import datetime


class Student(Person):
    Technique = models.CharField(max_length=255, choices=Techniques.choices)
    Course = models.CharField(max_length=255, choices=Course.choices)
    RNE = models.CharField(
        max_length=13, unique=True, default="JD05050000"
    )  # Campo RNE

    def save(self, *args, **kwargs):
        # Generación del campo RNE
        rne_parts = [
            self.First_Name[0].upper(),  # Primera letra del nombre en mayúscula
            self.Last_Name[0].upper(),  # Primera letra del primer apellido en mayúscula
            self.Sur_Name[0].upper(),  # Primera letra del segundo apellido en mayúscula
            str(self.Birthdate.year)[-2:],  # Año de nacimiento (últimos dos dígitos)
            str(self.Birthdate.month).zfill(2),  # Mes de nacimiento (dos dígitos)
            str(self.Birthdate.day).zfill(2),  # Día de nacimiento (dos dígitos)
            "0000",  # Cuatro ceros
        ]
        self.RNE = "".join(rne_parts)

        super().save(*args, **kwargs)  # Llama al método save de la clase padre
