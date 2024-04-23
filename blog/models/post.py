from django.db import models

# from pomaray.models.user import User
from .category import Category
from backend.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=200)
    description= models.CharField(max_length=300, default= "none description")
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    categories = models.ManyToManyField(Category)
    cover_photo = models.CharField(
        max_length=500, default="https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ="
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Puedes agregar otros campos como imagen destacada, etiquetas, etc.

    def __str__(self):
        return self.title
