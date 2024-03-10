from rest_framework import serializers
from library.models.Editorial import Editorial

class EditorialSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Editorial
        fields = '__all__'