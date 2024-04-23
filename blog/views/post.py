from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from backend.views import profile
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import HttpRequest
from blog.models.post import Post
from blog.serializers.post import PostSerializer
from django.db import connection


from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("EXEC GetPostList")
            rows = cursor.fetchall()

        data = []
        for row in rows:
            post_data = {
                "id": row[0],
                "title": row[1],
                "post_description": row[2],
                "post_cover_photo": row[3],
                "post_created_at": row[4],
                "post_updated_at": row[5],
                "author_name": row[6],
                "avatar_user": row[7],
                "category_name": row[8],
            }
            data.append(post_data)

        return Response(data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
