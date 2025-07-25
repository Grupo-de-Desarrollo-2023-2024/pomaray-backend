from rest_framework import serializers
from pomaray.models.employee import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        fields = '__all__'