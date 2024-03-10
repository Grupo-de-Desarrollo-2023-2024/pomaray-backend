from rest_framework import serializers
from library.models.Book import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = '__all__'