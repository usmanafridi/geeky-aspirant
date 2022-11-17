from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include('version_1.urls')) #This will accept all the endpoints of version_1 application
]

