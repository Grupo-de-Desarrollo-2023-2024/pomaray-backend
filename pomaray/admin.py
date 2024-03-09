from django.contrib import admin

from pomaray.models.student import Student
from pomaray.models.employee import Employee
from pomaray.models.department import Department

# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Department)