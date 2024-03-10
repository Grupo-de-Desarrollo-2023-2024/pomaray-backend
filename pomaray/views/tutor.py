from rest_framework import viewsets

from pomaray.models.tutor import Tutor
from pomaray.serializers.tutor import TutorSerializer


# Create your views here.


class TutorView(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()
