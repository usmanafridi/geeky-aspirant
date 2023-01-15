from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.profile),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("success/", views.success, name="success"),
    path("form/", views.contact, name="feedback_form"),

   

]
