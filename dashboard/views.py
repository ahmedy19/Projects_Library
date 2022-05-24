from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import DashboardUserCreationForm, ProjectCreateForm, SkillCreateForm, TagCreateForm
from accounts.models import Profile, Skill
from projects.models import Project, Tag


@login_required(login_url='accounts:signin')
def dash_home(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        projects = Project.objects.all().count()
        profiles = Profile.objects.all().count()
        skills = Skill.objects.all().count()
        tags = Tag.objects.all().count()
        students = Profile.objects.all().order_by('-created_at')[:10]
    else:
        messages.error(request, 'Where are you going!')
        return redirect('accounts:profiles')

    context = {
        'profile': profile,
        'profiles': profiles,
        'projects': projects,
        'skills': skills,
        'tags': tags,
        'students': students,
        
    }
    return render(request, 'dashboard/statistics.html', context)


@login_required(login_url='accounts:signin')
def all_students(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        students = Profile.objects.all().order_by('-created_at')
    else:
        messages.error(request, 'Where are you going!')
        return redirect('accounts:profiles')

    context = {
        'profile': profile,
        'students': students,
    }
    return render(request, 'dashboard/all_students.html', context)


@login_required(login_url='accounts:signin')
def all_skills(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        skills = Skill.objects.all().order_by('-created_at')
    else:
        messages.error(request, 'Where are you going!')
        return redirect('accounts:profiles')

    context = {
        'profile': profile,
        'skills': skills,
    }
    return render(request, 'dashboard/all_skills.html', context)


@login_required(login_url='accounts:signin')
def all_tags(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        tags = Tag.objects.all().order_by('-created_at')
    else:
        messages.error(request, 'Where are you going!')
        return redirect('accounts:profiles')

    context = {
        'profile': profile,
        'tags': tags,
    }
    return render(request, 'dashboard/all_tags.html', context)


@login_required(login_url='accounts:signin')
def all_projects(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        projects = Project.objects.all().order_by('-created_at')
    else:
        messages.error(request, 'Where are you going!')
        return redirect('accounts:profiles')

    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'dashboard/all_projects.html', context)


@login_required(login_url='accounts:signin')
def create_dash_account(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        try:
            form = DashboardUserCreationForm()
            if request.method == 'POST':
                form = DashboardUserCreationForm(request.POST or None)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.username = user.username.lower()
                    user.save()

                    messages.success(request, 'Account Successfully created 😀')
                    return redirect('dashboard:dash_home')
                else:
                    messages.error(request, 'Please, use your university email')

        except ObjectDoesNotExist:
            return redirect('dashboard:dash_home')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'dashboard/create_account.html', context)


@login_required(login_url='accounts:signin')
def create_project(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        try:
            form = ProjectCreateForm()
            if request.method == 'POST':
                form = ProjectCreateForm(request.POST or None, request.FILES or None)
                if form.is_valid():
                    project = form.save(commit=False)
                    project.owner = profile
                    project.save()

                    messages.success(request, 'Project created Successfully 😀')
                    return redirect('dashboard:all_projects')

        except ObjectDoesNotExist:
            return redirect('dashboard:all_projects')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'dashboard/create_project.html', context)


@login_required(login_url='accounts:signin')
def create_skill(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        try:
            form = SkillCreateForm()
            if request.method == 'POST':
                form = SkillCreateForm(request.POST or None)
                if form.is_valid():
                    skill = form.save(commit=False)
                    skill.owner = profile
                    skill.save()

                    messages.success(request, "Skill Created successfully")
                    return redirect('dashboard:all_skills')

        except ObjectDoesNotExist:
            return redirect('dashboard:all_skills')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'dashboard/create_skill.html', context)


@login_required(login_url='accounts:signin')
def create_tag(request):
    if request.user.is_authenticated and request.user.is_superuser:
        profile = request.user.profile

        try:
            form = TagCreateForm()
            if request.method == 'POST':
                form = TagCreateForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Tag created successfully")

                    return redirect('dashboard:all_tags')

        except ObjectDoesNotExist:
            return redirect('dashboard:all_tags')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'dashboard/create_tag.html', context)




