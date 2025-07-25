from rest_framework import serializers
from blog.models.post import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = '__all__'