from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .models import Profile, Skill
from .utils import profiles_pagination, search_profiles


def register_page(request):

    page = 'register'

    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'You are Successfully registered 😀')
            return redirect('accounts:signin')
        else:
            messages.error(request, 'Please, use your university email')

    context = {
        'page': page,
        'form': form,
    }

    return render(request, 'accounts/signin_signup.html', context)


def login_page(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('accounts:profiles')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:profiles')
        else:
            messages.error(request, 'Username or Password INCORRECT!')

    return render(request, 'accounts/signin_signup.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'You are Successfully logged out 😀')
    return redirect('accounts:profiles')


def profiles(request):

    profiles, search_query = search_profiles(request)
    custom_range, profiles = profiles_pagination(request, profiles, 6)

    context = {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'accounts/profiles.html', context)



def student_profile(request, id):

    profile = Profile.objects.get(pk=id)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {
        'profile': profile,
        'top_skills': top_skills,
        'other_skills': other_skills
    }
    return render(request, 'accounts/student_profile.html', context)


@login_required(login_url='accounts:signin')
def studnet_account(request):

    profile = request.user.profile

    skills = profile.skill_set.all() 
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    }

    return render(request, 'accounts/account.html', context)


@login_required(login_url='accounts:signin')
def edit_student_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('accounts:profiles')

    context = {
        'form': form
    }

    return render(request, 'accounts/profile_form.html', context)



@login_required(login_url='accounts:signin')
def create_skill(request):
    page_name = 'Create'
    
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST or None)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill created Successfully!')
            return redirect('accounts:account')

    context = {
        'form': form,
        'page_name': page_name,
    }

    return render(request, 'accounts/skill_form.html', context)


@login_required(login_url='accounts:signin')
def update_skill(request, id):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=id)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST or None, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated Successfully!')
            return redirect('accounts:account')

    context = {
        'form': form,    
    }
    return render(request, 'accounts/skill_form.html', context)


@login_required(login_url='accounts:signin')
def delete_skill(request, id):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=id)

    if request.method == 'POST':
        skill.delete()

        messages.success(request, 'Skill deleted Successfully!')
        return redirect('accounts:account') 

    context = {
        'object': skill
    }
    return render(request, 'delete_object.html', context)


def about(request):
    return render(request, 'about.html')
