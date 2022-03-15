from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
from accounts.models import Profile
from .utils import path_and_rename, path_and_rename_file, resize_image


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    supervisor = models.CharField(max_length=150, blank=True, null=True)
    project_image = models.ImageField(upload_to=path_and_rename, blank=True, null=True, default="default.jpg")
    demo_link = models.CharField(max_length=1000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    project_file = models.FileField(upload_to=path_and_rename_file, blank=True, null=True, validators=[FileExtensionValidator( ['zip'] ) ], default="default.zip")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        self.project_image = resize_image(self.project_image, size=(811, 403))

        super().save(*args, **kwargs)

