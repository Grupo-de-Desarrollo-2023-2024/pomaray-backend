from django.db import models
from .post import Post
from backend.models import CustomUser

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
