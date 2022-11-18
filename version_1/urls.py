from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("text-outline", views.outline),
    path("check", views.index),
    path("grammar", views.grammar_correction),
    path("summary", views.text_summarizer),
   

]



