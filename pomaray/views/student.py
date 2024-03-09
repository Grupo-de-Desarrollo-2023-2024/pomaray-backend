from rest_framework import viewsets

from pomaray.models.student import Student
from pomaray.serializers.student import StudentSerializer


# Create your views here.

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()