from django.contrib import admin
from .models.category import Category
from .models.comment import Comment
from .models.post import Post
# Register your models here.



admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
