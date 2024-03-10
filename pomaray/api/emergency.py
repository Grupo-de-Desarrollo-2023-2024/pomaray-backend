from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from pomaray.views.emergency import EmergencyView

router = routers.DefaultRouter()
router.register(r'emergency', EmergencyView, 'emergency')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Emergency API'))
]
