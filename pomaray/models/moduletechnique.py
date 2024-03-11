from django.db import models
from pomaray.utils.enums import Techniques


class ModuleTechnique(models.Model):
    module = models.CharField(max_length=100)
    technique = models.CharField(max_length=100, choices=Techniques.choices)
