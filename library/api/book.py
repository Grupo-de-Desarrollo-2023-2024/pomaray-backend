from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from library.views.Book import BookView

router = routers.DefaultRouter()
router.register(r'book', BookView, 'book')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Book API'))
]
