from rest_framework import serializers
from library.models.Author import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Author
        fields = '__all__'