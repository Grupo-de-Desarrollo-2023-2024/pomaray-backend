from rest_framework import serializers
from pomaray.models.moduletechnique import ModuleTechnique


class ModuleTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleTechnique
        fields = "__all__"
