from django.db import models
from pomaray.utils.models import Qualification
from pomaray.utils.enums import Subject
from pomaray.models.moduletechnique import ModuleTechnique

class academicQualification(Qualification):
    Subject = models.CharField(
        max_length=100, choices=Subject.choices, default=Subject.OTHER
    )
    P1 = models.IntegerField()
    P2 = models.IntegerField()
    P3 = models.IntegerField()
    P4 = models.IntegerField()

    def calculate_CF(self):
        # Calcula el valor de CF para acadmicQualification
        sumatoria = self.P1 + self.P2 + self.P3 + self.P4
        return sumatoria / 4  # Dividir la sumatoria por 4

    def save(self, *args, **kwargs):
        self.CF = self.calculate_CF()
        super(academicQualification, self).save(*args, **kwargs)


class tecnicQualification(Qualification):
    Module = models.ForeignKey(ModuleTechnique, on_delete=models.CASCADE)
    RA1 = models.IntegerField()
    RA2 = models.IntegerField()
    RA3 = models.IntegerField()
    RA4 = models.IntegerField()
    RA5 = models.IntegerField()
    RA6 = models.IntegerField()
    RA7 = models.IntegerField()
    RA8 = models.IntegerField()
    RA9 = models.IntegerField()
    RA10 = models.IntegerField()

    def calculate_CF(self):
       
        sumatoria = (
            self.RA1
            + self.RA2
            + self.RA3
            + self.RA4
            + self.RA5
            + self.RA6
            + self.RA7
            + self.RA8
            + self.RA9
            + self.RA10
        )
        return sumatoria   

    def save(self, *args, **kwargs):
        self.CF = self.calculate_CF()
        super(tecnicQualification, self).save(*args, **kwargs)
