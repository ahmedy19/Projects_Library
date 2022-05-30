from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/admin/signin', admin.site.urls),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('projects.urls', namespace='projects')),
    path('', include('dashboard.urls', namespace='dashboard')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
