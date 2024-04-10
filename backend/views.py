from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
import jwt, datetime
from django.views import View


@api_view(["POST"])
def login(request):
    try:
        user = User.objects.get(username=request.data["username"])
    except User.DoesNotExist:
        return Response(
            {"error": "Usuario con este nombre de usuario no existe."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not user.check_password(request.data["password"]):
        return Response(
            {"error": "Contraseña incorrecta."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
    serializer = UserSerializer(instance=user)
    response = Response()
    response.set_cookie(key="token", value=token, httponly=True)
    response.data = {"token": token, "user": serializer.data}
    return response


@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Verificamos la unicidad del correo electrónico
            email = serializer.validated_data["email"]
            if User.objects.filter(email=email).exists():
                return Response(
                    {"error": "Este correo electrónico ya está en uso."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Guardamos el usuario y creamos el token
            user = serializer.save()
            user.set_password(serializer.validated_data["password"])
            user.save()
            payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
            
            response = Response()
            
            response.set_cookie(key="token", value=token, httponly=True)
            
            response.data = {"token": token, "user": serializer.data}
            
            return response
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    if not request.user.is_authenticated:
        raise PermissionDenied({"message": "Unauthenticated!"})

    user = request.user

    response_data = {
        "id": user.id,
        "email": user.email,
        "username": user.username,
    }

    return Response(response_data)

class verifyToken(View):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise PermissionDenied({'message': 'Unauthenticated!'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise PermissionDenied({'message': 'Unauthenticated!'})

        try:
            user = User.objects.get(id=payload['id'])
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Unauthenticated!'})

        return JsonResponse({
            'id': user.id,
            'email': user.email,
            'username': user.username,
        })
