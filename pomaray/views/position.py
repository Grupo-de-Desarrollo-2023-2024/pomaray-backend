from rest_framework import viewsets

from pomaray.models.position import Cargo
from pomaray.serializers.position import PositionSerializer


# Create your views here.


class PositionView(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Cargo.objects.all()
