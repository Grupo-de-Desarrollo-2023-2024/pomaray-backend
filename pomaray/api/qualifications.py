from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from pomaray.views.qualifications import academicQualificationView, tecnicQualificationView

router = routers.DefaultRouter()
router.register(r'academicQualification', academicQualificationView, 'academicQualification')
router.register(r'tecnumQualificationView', tecnicQualificationView, 'tecnicQualification')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='academicQualification API')),
    path('docs/', include_docs_urls(title='tecnicQualification API'))
]
