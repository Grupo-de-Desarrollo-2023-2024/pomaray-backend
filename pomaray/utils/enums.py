from django.db import models


class Sex(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"


class Subject(models.TextChoices):
    MATH = "M", "Matemáticas"
    SCIENCE = "N", "Naturales"
    HISTORY = "S", "Sociales"
    ENGLISH = "I", "Inglés"
    SPANISH = "Ë", "Español"
    ART = (
        "A",
        "Arte",
    )
    PHYSICAL_EDUCATION = "ED", "Educación física"
    RELIGION = "REL", "Religión"
    OTHER = "O", "Other"


