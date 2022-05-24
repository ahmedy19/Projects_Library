"""Projects URL Configuration"""

from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('projects/project/project-<str:id>/', views.single_project, name="single_project"),
    path('projects/project/create-project', views.create_project, name="create_project"),
    path('projects/project/project-<str:id>/update', views.update_project, name="update_project"),
    path('projects/project/project-<str:id>/delete', views.delete_project, name="delete_project"),

]


handler404 = 'projects.views.error_page'



