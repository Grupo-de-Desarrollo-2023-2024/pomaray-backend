from rest_framework import serializers
from pomaray.models.gradesStudentView import StudentsGrades

class StudentsGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsGrades
        fields = '__all__'
