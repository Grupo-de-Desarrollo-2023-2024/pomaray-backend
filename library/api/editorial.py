from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from library.views.Editorial import EditorialView

router = routers.DefaultRouter()
router.register(r'editorial', EditorialView, 'editorial')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Editorial API'))
]
