from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Profile, Skill

admin.site.register(Profile)
admin.site.register(Skill)



admin.site.site_header = "Projects Library"
admin.site.site_title = "Projects Library Center"
admin.site.index_title = ""
LogEntry.objects.all().delete()
