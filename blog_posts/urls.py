from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.list_mobile),
    path('<int:id>/', views.retrieve_blog, name="blog-detail"),
   

]
