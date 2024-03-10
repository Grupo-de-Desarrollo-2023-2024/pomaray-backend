from rest_framework import viewsets

from library.models.Book import Book
from library.serializers.Book import BookSerializer


# Create your views here.


class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
