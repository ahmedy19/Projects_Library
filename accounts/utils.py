from io import BytesIO
from django.core.files import File
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from . import models
from PIL import Image
import os
from datetime import datetime


# Resize image
def resize_image(image, size=(100, 100)):
    """Resize image"""

    im = Image.open(image)
    im.convert('RGB')
    im.thumbnail(size)
    thumb_io = BytesIO()
    im.save(thumb_io, 'JPEG', quality=85)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail


# Select path and change name of uploaded image
def path_and_rename(instance, filename):
    """Select Path and Change name of image"""

    upload_to = 'profiles/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(datetime.now(), ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Pagination
def profiles_pagination(request, profiles, results):
    """Pagintion"""

    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles


# Search for Profiles
def search_profiles(request):
    """Search for Profiles"""

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = models.Skill.objects.filter(
        name__icontains=search_query
    ).order_by('-created_at')
    
    profiles = models.Profile.objects.distinct().filter(
        Q(first_name__icontains=search_query)|
        Q(last_name__icontains=search_query)| 
        Q(biography__icontains=search_query) | 
        Q(department__icontains=search_query) |
        Q(skill__in=skills)
    ).order_by('-created_at')

    return profiles, search_query
