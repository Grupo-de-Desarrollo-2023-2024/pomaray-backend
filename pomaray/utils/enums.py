from django.db import models


class Gender(models.TextChoices):
    MALE = "M", "Masculino"
    FEMALE = "F", "Femenino"
    OTHER = "O", "Otro"


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
    OTHER = "O", "Otro"


class Techniques(models.TextChoices):
    APP_DEVELOPMENT = "DAI", "Desarrollo y Administración de Aplicaciones Informáticas"
    TAX_ADMINISTRATION = "GAT", "Gestión y Administración Tributaria"
    TRADE_MARKETING = "CM", "Comercio y Mercadeo"
    GASTRONOMY = "G", "Gastronomía"
    ELECTRONICS = "E", "Electrónica"
    ELECTRICITY = "EL", "Electricidad"
    HVAC = "RAA", "Refrigeración y Acondicionamiento de Aire"
