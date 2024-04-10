from django.contrib import admin
from pomaray.models.emergency import Emergency

from pomaray.models.student import Student
from pomaray.models.employee import Employee
from pomaray.models.department import Department
from pomaray.models.position import Cargo
from pomaray.models.tutor import Tutor
from pomaray.models.activities import Activities
from pomaray.models.qualifications import tecnicQualification, academicQualification
from pomaray.models.moduletechnique import ModuleTechnique


# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Cargo)
admin.site.register(Tutor)
admin.site.register(Activities)
admin.site.register(Emergency)
admin.site.register(tecnicQualification)
admin.site.register(academicQualification)
admin.site.register(ModuleTechnique)
