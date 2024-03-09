from rest_framework import serializers
from pomaray.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = '__all__'