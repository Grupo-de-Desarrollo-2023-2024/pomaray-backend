from django.db import models
#from pomaray.models.user import User
from .category import Category
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    cover_photo = models.URLField(max_length=500, default="https://pbs.twimg.com/media/FOJS-LzXwAAV3aO.jpg:large")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Puedes agregar otros campos como imagen destacada, etiquetas, etc.

    def __str__(self):
        return self.title
