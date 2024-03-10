from rest_framework import viewsets

from pomaray.models.qualifications import academicQualification
from pomaray.serializers.qualifications import academicQualificationSerializer


# Create your views here.


class academicQualificationView(viewsets.ModelViewSet):
    serializer_class = academicQualificationSerializer
    queryset = academicQualification.objects.all()
