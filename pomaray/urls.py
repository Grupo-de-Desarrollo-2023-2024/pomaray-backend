from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from pomaray import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentView, 'students')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Student API'))
]
