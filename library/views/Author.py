from rest_framework import viewsets

from library.models.Author import Author
from library.serializers.Author import AuthorSerializer


# Create your views here.


class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
