from rest_framework import serializers
from backend.models import CustomUser
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'email': {'validators': []},  
        }

    def validate_email(self, value):
        """
        Método de validación personalizado para el campo email.
        Verifica si el correo electrónico ya existe en la base de datos.
        """
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        return value

