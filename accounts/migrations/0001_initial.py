# Generated by Django 4.0.3 on 2022-03-06 22:09

import accounts.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('uni_email', models.EmailField(blank=True, max_length=400, null=True, unique=True)),
                ('identity_number', models.PositiveBigIntegerField(blank=True, null=True, unique=True)),
                ('department', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Information Technology', 'Information Technology'), ('Network', 'Network')], default='Computer Science', max_length=25)),
                ('biography', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to=accounts.utils.path_and_rename)),
                ('facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
