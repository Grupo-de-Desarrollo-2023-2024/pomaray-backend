from rest_framework import serializers
from pomaray.models.qualifications import academicQualification

class academicQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = academicQualification
        fields = '__all__'
