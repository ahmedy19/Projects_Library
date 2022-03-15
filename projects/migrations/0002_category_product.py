# Generated by Django 4.0.3 on 2022-03-10 19:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import projects.utils
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_skill'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('supervisor', models.CharField(blank=True, max_length=150, null=True)),
                ('project_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to=projects.utils.path_and_rename)),
                ('demo_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('project_file', models.FileField(blank=True, default='default.zip', null=True, upload_to=projects.utils.path_and_rename_file, validators=[django.core.validators.FileExtensionValidator(['zip'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.profile')),
                ('tags', models.ManyToManyField(blank=True, to='projects.category')),
            ],
        ),
    ]
