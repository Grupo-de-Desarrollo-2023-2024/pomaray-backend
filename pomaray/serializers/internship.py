from rest_framework import serializers
from pomaray.models.internship import Internship

class InternshipSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Internship
        fields = '__all__'