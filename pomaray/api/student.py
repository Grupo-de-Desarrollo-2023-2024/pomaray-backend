from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from pomaray.views.student import StudentView

router = routers.DefaultRouter()
router.register(r'students', StudentView, 'students')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Student API'))
]
