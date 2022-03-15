"""Accounts URL Configuration"""

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('auth/login/', views.login_page, name="signin"),
    path('auth/logout', views.logout_page, name="logout"),
    path('auth/register/', views.register_page, name="signup"),

    path('', views.profiles, name="profiles"),
    path('student/profile/profile-<str:id>/', views.student_profile, name="student"),
    path('student/', views.studnet_account, name="account"),
    path('student/edit/', views.edit_student_account, name="edit_account"),
    path('skills/create/', views.create_skill, name="create_skill"),
    path('skills/skill/skill-<str:id>/update', views.update_skill, name="update_skill"),
    path('skills/skill/skill-<str:id>/delete', views.delete_skill, name="delete_skill"),
    path('about/', views.about, name="about"),

]