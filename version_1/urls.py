from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("text-outline", views.outline),
    # path("check", views.index),
    path("grammar", views.grammar_correction, name="grammar"),
    path("summary", views.text_summarizer, name="summary"),
    path("sentence", views.word_mean_sentence),
    path("", views.index),
    path("syn_ant", views.syn_anto, name="synonym"),
    path("fill", views.fill_the_blank),
    path("translate", views.translate, name="translate"),
    path("comprehension", views.comprehension, name="comprehension"),
    ## This is for contact information
    
    path("contact/", views.contactView, name="contact"),
    path("success/", views.successView, name="success"),

]


## Link for the website from which the contact form was taken. 

## https://learndjango.com/tutorials/django-email-contact-form