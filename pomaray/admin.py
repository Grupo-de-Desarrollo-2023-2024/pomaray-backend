from django.contrib import admin
from pomaray.models.emergency import Emergency

from pomaray.models.student import Student
from pomaray.models.employee import Employee
from pomaray.models.department import Department
from pomaray.models.position import Cargo
from pomaray.models.tutor import Tutor
from pomaray.models.activities import Activities
from pomaray.models.internship import Internship

# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Cargo)
admin.site.register(Tutor)
admin.site.register(Activities)
<<<<<<< HEAD
admin.site.register(Internship)
=======
admin.site.register(Emergency)
>>>>>>> 3f7d46e6d53c52ab09ffd40d8023f92017a315e1
