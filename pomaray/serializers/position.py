from rest_framework import serializers
from pomaray.models.position import Cargo

class PositionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cargo
        fields = '__all__'