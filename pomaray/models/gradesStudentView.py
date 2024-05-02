from django.db import models

class StudentsGrades(models.Model):
    id = models.IntegerField(primary_key=True)
    Photo_URL = models.CharField(max_length=4000)
    full_name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    p1 = models.FloatField()
    p2 = models.FloatField()
    p3 = models.FloatField()
    p4 = models.FloatField()
    cf = models.FloatField()

    class Meta:
        managed = False  # Le indicamos a Django que no debe gestionar esta tabla, ya que es una vista.
        db_table = 'Students_Grades'  # Nombre de la vista en la base de datos
