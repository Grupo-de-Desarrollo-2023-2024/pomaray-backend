from rest_framework import serializers
from pomaray.models.emergency import Emergency

class EmergencySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Emergency
        fields = '__all__'