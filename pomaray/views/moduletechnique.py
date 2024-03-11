from rest_framework import viewsets

from pomaray.models.moduletechnique import ModuleTechnique
from pomaray.serializers.moduletechnique import ModuleTechniqueSerializer


class ModuleTechniqueView(viewsets.ModelViewSet):
    serializer_class = ModuleTechniqueSerializer
    queryset = ModuleTechnique.objects.all()
