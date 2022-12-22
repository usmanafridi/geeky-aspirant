from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include('version_1.urls')), #This will accept all the endpoints of version_1 application
    path("profile/", include('users.urls')),
    path("blogs/", include('blog_posts.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)