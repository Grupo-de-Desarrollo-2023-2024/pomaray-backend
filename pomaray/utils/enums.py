from django.db import models



class Gender(models.TextChoices):
    MALE = "M", "Masculino"
    FEMALE = "F", "Femenino"


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


# Asegúrate de importar correctamente tu modelo


class Course(models.TextChoices):
    # Informática
    FOURTH_DAI_A = (
        "4_DAI_A",
        "4to Desarrollo y Administración de Aplicaciones Informáticas Sección A",
    )
    FIFTH_DAI_A = (
        "5_DAI_A",
        "5to Desarrollo y Administración de Aplicaciones Informáticas Sección A",
    )
    SIXTH_DAI_A = (
        "6_DAI_A",
        "6to Desarrollo y Administración de Aplicaciones Informáticas Sección A",
    )

    # Contabilidad
    FOURTH_GAT_A = "4_GAT_A", "4to Gestión y Administración Tributaria Sección A"
    FOURTH_GAT_B = "4_GAT_B", "4to Gestión y Administración Tributaria Sección B"

    FIFTH_GAT_A = "5_GAT_A", "5to Gestión y Administración Tributaria Sección A"
    FIFTH_GAT_B = "5_GAT_B", "5to Gestión y Administración Tributaria Sección B"

    SIXTH_GAT_A = "6_GAT_A", "6to Gestión y Administración Tributaria Sección A"
    SIXTH_GAT_B = "6_GAT_B", "6to Gestión y Administración Tributaria Sección B"

    # Comercio y Mercadeo
    FOURTH_CM_A = "4_CM_A", "4to Comercio y Mercadeo Sección A"
    FOURTH_CM_B = "4_CM_B", "4to Comercio y Mercadeo Sección B"

    FIFTH_CM_A = "5_CM_A", "5to Comercio y Mercadeo Sección A"
    FIFTH_CM_B = "5_CM_B", "5to Comercio y Mercadeo Sección B"

    SIXTH_CM_A = "6_CM_A", "6to Comercio y Mercadeo Sección A"
    SIXTH_CM_B = "6_CM_B", "6to Comercio y Mercadeo Sección B"

    # Gastronomía
    FOURTH_G_A = "4_G_A", "4to Gastronomía Sección A"

    FIFTH_G_A = "5_G_A", "5to Gastronomía Sección A"

    SIXTH_G_A = "6_G_A", "6to Gastronomía Sección A"

    # Electrónica
    FOURTH_E_A = "4_E_A", "4to Electrónica Sección A"

    FIFTH_E_A = "5_E_A", "5to Electrónica Sección A"

    SIXTH_E_A = "6_E_A", "6to Electrónica Sección A"

    # Electricidad
    FOURTH_EL_A = "4_EL_A", "4to Electricidad Sección A"

    FIFTH_EL_A = "5_EL_A", "5to Electricidad Sección A"

    SIXTH_EL_A = "6_EL_A", "6to Electricidad Sección A"

    # HVAC
    FOURTH_RAA_A = "4_RAA_A", "4to Refrigeración y Acondicionamiento de Aire Sección A"

    FIFTH_RAA_A = "5_RAA_A", "5to Refrigeración y Acondicionamiento de Aire Sección A"

    SIXTH_RAA_A = "6_RAA_A", "6to Refrigeración y Acondicionamiento de Aire Sección A"

class Departments(models.TextChoices):
    HUMAN_RESOURCES = "HR", "Recursos Humanos"
    ACCOUNTANTS = "ACCS", "Finanzas y Contabilidad"
    REGISTER = "RGS","Admisiones y Registro"
    MAINTENANCE = "MTE","Limpieza y Mantenimiento"
    SECURITY = "SCY", "Seguridad y Bienestar"
    PSYCHOLOGY = "PSY", "Psicologia"
    VINCULATION = "VCN", "Vinculación Sectorial"
    ADMINISTRATIVE = "ADT", "Administracion y Coordinación"
    EDUCATION = "EDT", "Docencia"
    LIBRARY = "LBR", "Biblioteca"

class Positions(models.TextChoices):
    PRINCIPAL = "PR", "Director"
    SECRETARY = "SCT","Secretaria"
    TEACHER = "TEA","Profesor"
    PSYCHOLOGIST = "PSY", "Psicologo"
    LIBRARIAN = "LBR", "Bibliotecario"
    JANITOR = "JNR", "Conserje"
    SUPERVISOR = "SPR", "Encargado"
    SECURITY_GUARD = "SCG", "Guardia de Seguridad"