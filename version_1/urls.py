from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("text-outline", views.outline),
    # path("check", views.index),
    path("grammar", views.grammar_correction),
    path("summary", views.text_summarizer),
    path("sentence", views.word_mean_sentence),
    path("", views.index),
    path("syn_ant", views.syn_anto),
    path("fill", views.fill_the_blank),
   

]
