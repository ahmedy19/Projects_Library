from io import BytesIO
from django.core.files import File
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from . import models
import uuid
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

    upload_to = 'projects/'
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(datetime.now(), ext)
    
    return os.path.join(upload_to, filename)


# Select path and change name of uploaded image
def path_and_rename_file(instance, filename):
    """Select Path and Change name of image"""

    upload_to = 'projects_file/'
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = '{}.{}'.format(str(uuid.uuid4().hex) + str(instance.pk), ext)
    else:
        filename = '{}.{}'.format(datetime.now(), ext)
    
    return os.path.join(upload_to, filename)


# Pagination
def projects_pagination(request, projects, results):
    """Pagintion"""

    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects


# Search for Projects
def search_project(request):
    """Search for Projects"""

    search_query = ''

    if request.GET.get('search'):
        search_query = request.GET.get('search')
    
    tags = models.Tag.objects.filter(
        name__icontains=search_query
    ).order_by('-created_at')

    projects = models.Project.objects.distinct().filter(
        Q(title__icontains=search_query) | 
        Q(supervisor__icontains=search_query) | 
        Q(description__icontains=search_query) |
        Q(owner__first_name__icontains=search_query) |
        Q(tags__in=tags)
    ).order_by('-created_at')

    return projects, search_query




