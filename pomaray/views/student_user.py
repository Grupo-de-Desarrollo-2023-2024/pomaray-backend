from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from pomaray.models.student import Student
from backend.models import CustomUser
from backend.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["POST"])
def create_student_user(request):
    if request.method == "POST":
        rne = request.data.get("rne")
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        student = get_object_or_404(Student, RNE=rne)

        if CustomUser.objects.filter(username=username).exists():
            return Response(
                {"error": "Ya existe un usuario con este nombre de usuario."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = CustomUser.objects.create_user(
            username=username, email=email, password=password
        )

        # Generar tokens para el nuevo usuario
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Asociar el usuario al estudiante
        student.user = user
        student.save()

        # Serializar el usuario y los tokens y retornarlos
        serializer = UserSerializer(user)
        return Response(
            {"user": serializer.data, "access_token": access_token},
            status=status.HTTP_201_CREATED,
        )

    return Response(
        {"error": "Método no permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )
