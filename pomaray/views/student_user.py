from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from pomaray.models.student import Student
from backend.models import CustomUser
from backend.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def create_student_user(request):
    if request.method == "POST":
        rne = request.data.get(
            "rne"
        )  # Obtener el RNE del estudiante desde los datos de la solicitud
        username = request.data.get(
            "username"
        )  # Obtener el nombre de usuario desde los datos de la solicitud
        email = request.data.get("email")
        password = request.data.get(
            "password"
        )  # Obtener la contraseña desde los datos de la solicitud

        # Buscar el estudiante correspondiente usando el RNE
        student = get_object_or_404(Student, RNE=rne)

        # Verificar si ya existe un usuario con el mismo nombre de usuario
        if CustomUser.objects.filter(username=username).exists():
            return Response(
                {"error": "Ya existe un usuario con este nombre de usuario."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Crear el nuevo usuario
        user = CustomUser.objects.create_user(
            username=username, email=email, password=password
        )

        # Asociar el usuario al estudiante
        student.user = user
        student.save()

        # Serializar el usuario y retornar los datos
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(
        {"error": "Método no permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )
