from rest_framework import serializers
from pomaray.models.qualifications import academicQualification, tecnicQualification

class academicQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = academicQualification
        fields = '__all__'
        
        
class tecnicQualificationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = tecnicQualification
        fields = '__all__'

