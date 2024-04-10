from rest_framework import viewsets

from blog.models.category import Category
from blog.serializers.category import CategorySerializer


# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
