from rest_framework import viewsets

from pomaray.models.qualifications import academicQualification, tecnicQualification
from pomaray.serializers.qualifications import academicQualificationSerializer, tecnicQualificationSerializer


# Create your views here.


class academicQualificationView(viewsets.ModelViewSet):
    serializer_class = academicQualificationSerializer
    queryset = academicQualification.objects.all()


class tecnicQualificationView(viewsets.ModelViewSet):
    serializer_class = tecnicQualificationSerializer
    queryset = tecnicQualification.objects.all()