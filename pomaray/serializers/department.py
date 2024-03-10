from rest_framework import serializers
from pomaray.models.department import Department

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Department
        fields = '__all__'