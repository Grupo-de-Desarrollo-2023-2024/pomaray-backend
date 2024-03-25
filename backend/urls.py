from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("pomaray.api.urls")),
    path("employees/", include("pomaray.api.urls")),
    path("department/", include("pomaray.api.urls")),
    path("academicQualification/", include("pomaray.api.urls")),
    path("tecnicQualification/", include("pomaray.api.urls")),
    path("position/", include("pomaray.api.urls")),
    path("tutor/", include("pomaray.api.urls")),
    path("internship/", include("pomaray.api.urls")),
    path("emergency/", include("pomaray.api.urls")),
    path("activities/", include("pomaray.api.urls")),
    path("book/", include("library.api.urls")),
    path("editorial/", include("library.api.urls")),
    path("author/", include("library.api.urls")),
    path("loan/", include("library.api.urls")),
    
   
]
