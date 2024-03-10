from rest_framework import viewsets

from pomaray.models.department import Department
from pomaray.serializers.department import DepartamentSerializer


# Create your views here.


class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DepartamentSerializer
    queryset = Department.objects.all()
