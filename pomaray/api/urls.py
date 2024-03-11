from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from pomaray.views.activities import ActivitiesView
from pomaray.views.department import DepartmentView
from pomaray.views.emergency import EmergencyView
from pomaray.views.employee import EmployeeView
from pomaray.views.internship import InternshipView
from pomaray.views.position import PositionView
from pomaray.views.qualifications import (
    academicQualificationView,
    tecnicQualificationView,
)
from pomaray.views.student import StudentView
from pomaray.views.tutor import TutorView
from pomaray.views.moduletechnique import ModuleTechniqueView

router = routers.DefaultRouter()
router.register(r"tutor", TutorView, "tutor")
router.register(r"activities", ActivitiesView, "activities")
router.register(r"department", DepartmentView, "department")
router.register(r"emergency", EmergencyView, "emergency")
router.register(r"employees", EmployeeView, "employees")
router.register(r"internship", InternshipView, "internship")
router.register(r"position", PositionView, "position")
router.register(
    r"academicQualification", academicQualificationView, "academicQualification"
)
router.register(r"tecnicQualification", tecnicQualificationView, "tecnicQualification")
router.register(r"students", StudentView, "students")
router.register(r"moduleTechnique", ModuleTechniqueView , "moduleTechnique")


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/tutor", include_docs_urls(title="Tutor API")),
    path("docs/activities", include_docs_urls(title="Activities API")),
    path("docs/departement", include_docs_urls(title="Department API")),
    path("docs/emergency", include_docs_urls(title="Emergency API")),
    path("docs/employee", include_docs_urls(title="Employee API")),
    path("docs/intership", include_docs_urls(title="Internship API")),
    path("docs/position", include_docs_urls(title="Position API")),
    path("docs/academic", include_docs_urls(title="academicQualification API")),
    path("docs/tecnic/tecnic", include_docs_urls(title="tecnicQualification API")),
    path("docs/moduleTechnique", include_docs_urls(title="moduleTechnique API")),
]
