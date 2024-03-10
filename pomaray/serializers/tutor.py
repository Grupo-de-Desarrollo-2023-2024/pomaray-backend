from rest_framework import serializers
from pomaray.models.tutor import Tutor

class TutorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tutor
        fields = '__all__'