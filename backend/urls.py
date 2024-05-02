from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from pomaray.views import student_user
from blog.views import post
from pomaray.views.gradesStudentView import AllStudentsGradesView, StudentGradesView
urlpatterns = [
    path("admin/", admin.site.urls),
    
    #POMARAY URLS
    path("students/", include("pomaray.api.urls")),
    path('students-grades/<int:student_id>/', StudentGradesView.as_view(), name='students_grades'),
    path('students-grades/', AllStudentsGradesView.as_view(), name='all_students_grades'),
    path("employees/", include("pomaray.api.urls")),
    path("department/", include("pomaray.api.urls")),
    path("academicQualification/", include("pomaray.api.urls")),
    path("tecnicQualification/", include("pomaray.api.urls")),
    path("position/", include("pomaray.api.urls")),
    path("tutor/", include("pomaray.api.urls")),
    path("internship/", include("pomaray.api.urls")),
    path("emergency/", include("pomaray.api.urls")),
    #LIBRARY_URL
    path("activities/", include("pomaray.api.urls")),
    path("book/", include("library.api.urls")),
    path("editorial/", include("library.api.urls")),
    path("author/", include("library.api.urls")),
    path("loan/", include("library.api.urls")),
    #BLOG_URL
    path("comment/", include("blog.api.urls")),
    path("post/", post.post_list, name="post-list"),
    path("post/<int:pk>/", post.post_detail, name="post-detail"),
    path("category/", include("blog.api.urls")),
    
    #AUTH URL
    path('login/', views.student_login),
     path('admin/login/', views.admin_login),
    path('register/', views.register),
    path('profile/', views.profile),
    path('student/user/',student_user.create_student_user), 

  
    
    
]
