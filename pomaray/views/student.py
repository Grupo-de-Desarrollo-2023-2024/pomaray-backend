from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from pomaray.models.student import Student
from pomaray.serializers.student import StudentSerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

   