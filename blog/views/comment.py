from rest_framework import viewsets

from blog.models.comment import Comment
from blog.serializers.comment import CommentSerializer


# Create your views here.


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
