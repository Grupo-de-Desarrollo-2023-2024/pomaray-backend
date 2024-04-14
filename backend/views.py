from rest_framework.decorators import (
    api_view,
    authentication_classes,
)
from .serializers import UserSerializer
from datetime import timedelta
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken


token_lifetime = timedelta(hours=1)


def set_access_token_cookie(response, access_token):
    response.set_cookie(key="access_token", value=str(access_token), httponly=True)


@api_view(["POST"])
def login(request):
    try:
        user = User.objects.get(username=request.data["username"])
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "Usuario con este nombre de usuario no existe."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not user.check_password(request.data["password"]):
        return JsonResponse(
            {"error": "Contraseña incorrecta."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    access_token = AccessToken.for_user(user)
    access_token.set_exp(lifetime=token_lifetime)

    serializer = UserSerializer(instance=user)
    response = JsonResponse(
        {"access_token": str(access_token), "user": serializer.data}
    )
    set_access_token_cookie(response, access_token)
    return response


@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            if User.objects.filter(email=email).exists():
                return JsonResponse(
                    {"error": "Este correo electrónico ya está en uso."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = serializer.save()
            user.set_password(serializer.validated_data["password"])
            user.save()

            access_token = AccessToken.for_user(user)

            response = JsonResponse()
            set_access_token_cookie(response, access_token)
            return response

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def profile(request):
    user = request.user
    try:
        token = request.COOKIES.get("access_token")
        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        access_token = AccessToken(token)
        payload = access_token.payload

        user_id = payload.get("user_id")
        user = User.objects.get(id=user_id)

        return JsonResponse(
            {
                "id": user.id,
                "email": user.email,
                "username": user.username,
            }
        )
    except (InvalidToken, TokenError):
        raise AuthenticationFailed("Unauthenticated!")

    except User.DoesNotExist:
        raise AuthenticationFailed("Unauthenticated!")
