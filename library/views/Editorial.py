from rest_framework import viewsets

from library.models.Editorial import Editorial
from library.serializers.Editorial import EditorialSerializer


# Create your views here.


class EditorialView(viewsets.ModelViewSet):
    serializer_class = EditorialSerializer
    queryset = Editorial.objects.all()
