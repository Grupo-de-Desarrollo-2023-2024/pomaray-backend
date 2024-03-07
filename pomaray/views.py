from rest_framework import viewsets

from pomaray.models import Student
from pomaray.serializer import StudentSerializer


# Create your views here.

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()