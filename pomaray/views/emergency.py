from rest_framework import viewsets

from pomaray.models.emergency import Emergency
from pomaray.serializers.emergency import EmergencySerializer


# Create your views here.


class EmergencyView(viewsets.ModelViewSet):
    serializer_class = EmergencySerializer
    queryset = Emergency.objects.all()
