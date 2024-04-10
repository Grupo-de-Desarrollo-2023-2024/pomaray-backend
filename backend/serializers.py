from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
           "groups"
        ]
        extra_kwargs = {
            'email': {'validators': []},  
        }

    def validate_email(self, value):
        """
        Método de validación personalizado para el campo email.
        Verifica si el correo electrónico ya existe en la base de datos.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        return value

