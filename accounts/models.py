from django.db import models
import uuid
from django.contrib.auth.models import User
from .utils import path_and_rename, resize_image


class Profile(models.Model):

    COMPUTER_SCIENCE = 'Computer Science'
    INFORMATION_TECHNOLOGY = 'Information Technology'
    NETWORK = 'Network'

    DEPARTMENTS = [
        (COMPUTER_SCIENCE, 'Computer Science'),
        (INFORMATION_TECHNOLOGY, 'Information Technology'),
        (NETWORK, 'Network')
    ]


    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    uni_email = models.EmailField(max_length=400, blank=True, null=True, unique=True)
    identity_number = models.PositiveBigIntegerField(unique=True, blank=True, null=True)
    department = models.CharField(max_length=25, choices=DEPARTMENTS, default=COMPUTER_SCIENCE,)
    biography = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to=path_and_rename, blank=True, null=True, default="avatar.jpg")
    facebook = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)
    

    def save(self, *args, **kwargs):
        self.profile_image = resize_image(self.profile_image, size=(460, 460))

        super().save(*args, **kwargs)


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


