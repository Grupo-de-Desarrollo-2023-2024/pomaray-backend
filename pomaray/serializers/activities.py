from rest_framework import serializers
from pomaray.models.activities import Activities

#torei y papia eh eh eh

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Activities
        fields = '__all__'