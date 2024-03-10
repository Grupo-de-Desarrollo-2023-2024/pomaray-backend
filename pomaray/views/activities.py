from rest_framework import viewsets

from pomaray.models.activities import Activities
from pomaray.serializers.activities import ActivitiesSerializer


# Create your views here.


class ActivitiesView(viewsets.ModelViewSet):
    serializer_class = ActivitiesSerializer
    queryset = Activities.objects.all()
