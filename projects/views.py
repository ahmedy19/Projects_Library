from django.shortcuts import render, redirect
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Tag
from .forms import ProjectForm
from .utils import search_project, projects_pagination


def projects(request):

    projects, search_query = search_project(request)
    custom_range, projects = projects_pagination(request, projects, 9)

    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range,
    }

    return render(request, 'projects/projects.html', context)


def single_project(request, id):
    project = Project.objects.get(pk=id)
    tags = project.tags.all()

    context = {
        'project': project,
        'tags': tags
    }

    return render(request, 'projects/single_project.html', context)


@login_required(login_url="accounts:signin")
def create_project(request):
    page_name = 'Create'

    profile = request.user.profile

    tags = Tag.objects.all()

    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            messages.success(request, 'Project Successfully created 😀')
            return redirect('projects:projects')

    context = {
        'form': form,
        'page_name': page_name,
    }

    return render(request, 'projects/project_form.html', context)


@login_required(login_url="accounts:signin")
def update_project(request, id):
    profile = request.user.profile
    project = profile.project_set.get(pk=id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()

            messages.success(request, 'Project Successfully updated 😀')
            return redirect('projects:projects')

    context = {
        'form': form
    }

    return render(request, 'projects/project_form.html', context)


@login_required(login_url="accounts:signin")
def delete_project(request, id):
    profile = request.user.profile
    project = profile.project_set.get(pk=id)

    if request.method == 'POST':
        if len(project.project_image) > 0 and len(project.project_file) > 0:
            os.remove(project.project_image.path)
            os.remove(project.project_file.path)
        project.delete()

        messages.success(request, 'Project Successfully deleted 😀')
        return redirect('projects:projects')

    context = {
        'object': project
    }
    return render(request, 'delete_object.html', context)


# 404 error page
def error_page(request, exception):
    return render(request,'404.html', status=404)

