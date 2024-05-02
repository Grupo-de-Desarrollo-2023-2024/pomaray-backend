from rest_framework import generics
from pomaray.models.gradesStudentView import StudentsGrades
from pomaray.serializers.gradesStudentView import StudentsGradesSerializer
from django.views import View
from django.http import JsonResponse


class StudentGradesView(View):
    def get(self, request, student_id):
        try:
            # Filtrar las calificaciones del estudiante por su ID
            grades = StudentsGrades.objects.filter(id=student_id)

            # Verificar si el estudiante existe
            if not grades.exists():
                return JsonResponse({"error": "Estudiante no encontrado"}, status=404)

            # Construir el JSON combinado
            student_data = {
                "id": grades[0].id,
                "Photo_URL": grades[0].Photo_URL,
                "full_name": grades[0].full_name,
                "course": grades[0].course,
                "period": grades[0].period,
                "grades": [],
            }

            for grade in grades:
                grade_data = {
                    "subject": grade.subject,
                    "p1": grade.p1,
                    "p2": grade.p2,
                    "p3": grade.p3,
                    "p4": grade.p4,
                    "cf": grade.cf,
                }
                student_data["grades"].append(grade_data)

            return JsonResponse(student_data)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


class AllStudentsGradesView(View):
    def get(self, request):
        try:
            # Obtener todos los datos de todos los estudiantes y sus calificaciones
            all_students_grades = StudentsGrades.objects.all()
            
            # Lista para almacenar los datos de todos los estudiantes
            all_students_data = []
            
            # Iterar sobre cada estudiante y sus calificaciones
            for student in all_students_grades:
                student_data = {
                    'id': student.id,
                    'Photo_URL': student.Photo_URL,
                    'full_name': student.full_name,
                    'course': student.course,
                    'period': student.period,
                    'grades': [
                        {
                            'subject': 'ED',
                            'p1': student.p1,
                            'p2': student.p2,
                            'p3': student.p3,
                            'p4': student.p4,
                            'cf': student.cf
                        },
                        {
                            'subject': 'M',
                            'p1': student.p1,
                            'p2': student.p2,
                            'p3': student.p3,
                            'p4': student.p4,
                            'cf': student.cf
                        },
                        {
                            'subject': 'Ë',
                            'p1': student.p1,
                            'p2': student.p2,
                            'p3': student.p3,
                            'p4': student.p4,
                            'cf': student.cf
                        }
                    ]
                }
                all_students_data.append(student_data)
            
            return JsonResponse(all_students_data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)