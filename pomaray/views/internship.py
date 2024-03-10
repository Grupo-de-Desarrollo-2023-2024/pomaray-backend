from rest_framework import viewsets

from pomaray.models.internship import Internship
from pomaray.serializers.internship import InternshipSerializer


# Create your views here.


class InternshipView(viewsets.ModelViewSet):
    serializer_class = InternshipSerializer
    queryset = Internship.objects.all()
