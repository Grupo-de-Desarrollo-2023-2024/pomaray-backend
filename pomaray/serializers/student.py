from rest_framework import serializers
from pomaray.models.student import Student

#torei y papia eh eh eh

class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = '__all__'