from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from blog.views.category import CategoryView
from blog.views.comment import CommentView



router = routers.DefaultRouter()
router.register(r"category", CategoryView, "category")
router.register(r"comment", CommentView, "comment")


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/category/", include_docs_urls(title="Category API")),
    path("docs/Comment/", include_docs_urls(title="Comment API")),

]
