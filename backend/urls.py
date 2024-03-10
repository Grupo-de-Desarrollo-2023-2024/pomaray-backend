"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("pomaray.api.student")),
    path("employees/", include("pomaray.api.employee")),
    path("department/", include("pomaray.api.department")),
    path("position/", include("pomaray.api.position")),
    path("tutor/", include("pomaray.api.tutor")),
<<<<<<< HEAD
    path("tutor/", include("pomaray.api.activities")),
    path("internship/", include("pomaray.api.internship")),
=======
    path("emergency/", include("pomaray.api.emergency")),
    path("activities/", include("pomaray.api.activities")),
>>>>>>> 3f7d46e6d53c52ab09ffd40d8023f92017a315e1
    path("book/", include("library.api.book")),
    path("editorial/", include("library.api.editorial")),
    path("author/", include("library.api.author")),
    path("loan/", include("library.api.loan")),
   
]
