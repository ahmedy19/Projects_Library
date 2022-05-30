"""Dashboard URL Configuration"""

from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('auth/dashboard/', views.dash_home, name="dash_home"),
    path('auth/dashboard/all-students/', views.all_students, name="all_students"),
    path('auth/dashboard/all-skills/', views.all_skills, name="all_skills"),
    path('auth/dashboard/all-tags/', views.all_tags, name="all_tags"),
    path('auth/dashboard/all-projects/', views.all_projects, name="all_projects"),

    path('auth/dashboard/create-user-account/', views.create_dash_account, name="create_dash_account"),
    path('auth/dashboard/create-skill/', views.create_skill, name="create_skill"),
    path('auth/dashboard/create-tag/', views.create_tag, name="create_tag"),
    path('auth/dashboard/create-project/', views.create_project, name="create_project"),

    path('auth/dashboard/student-<str:id>/details', views.dash_student_details, name="dash_view_student"),
    path('auth/dashboard/skill-<str:id>/details', views.dash_skill_details, name="dash_view_skill"),path('auth/dashboard/project-<str:id>/details', views.dash_project_details, name="dash_view_project"),

    path('auth/dashboard/student-<str:id>/delete', views.dash_delete_student, name="dash_delete_student"),
    path('auth/dashboard/skill-<str:id>/delete', views.dash_delete_skill, name="dash_delete_skill"),
    path('auth/dashboard/tag-<str:id>/delete', views.dash_delete_tag, name="dash_delete_tag"),
    path('auth/dashboard/project-<str:id>/delete', views.dash_delete_project, name="dash_delete_project"),

]






