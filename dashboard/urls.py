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

]






