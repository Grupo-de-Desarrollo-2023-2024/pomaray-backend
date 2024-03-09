from rest_framework import viewsets

from pomaray.models.employee import Employee
from pomaray.serializers.employee import EmployeeSerializer


# Create your views here.


class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
