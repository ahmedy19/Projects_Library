from django.contrib import admin
from .models import Tag, Project


admin.site.register(Project)
admin.site.register(Tag)

