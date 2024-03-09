from django.db import models
from pomaray.utils.models import Qualification


class acadmicQualification:
    subject = models.ForeignKey
    P1 = models.IntegerField()
    P2 = models.IntegerField()
    P3 = models.IntegerField()
    P4 = models.IntegerField()


class tecnicQualification:
    Module = models.CharField(max_length=100)
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
