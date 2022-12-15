from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("text-outline", views.outline, name="text_outline"),
    # path("check", views.index),
    path("grammar", views.grammar_correction, name="grammar"),
    path("summary", views.text_summarizer, name="summary"),
    path("sentence", views.word_mean_sentence),
    path("", views.index),
    path("syn_ant", views.syn_anto, name="synonym"),
    path("fill", views.fill_the_blank),
    path("translate", views.translate, name="translate"),
    path("comprehension", views.comprehension_updated, name="comprehension"),
    path("speech", views.speech_change, name="speech"),
    
    ## This is for contact information
    
    path("contact/", views.contactView, name="contact"),
    path("success/", views.successView, name="success"),

]





## Give prior Prompt examples so that it can pick it up easy, and that the results are good in production.


## Only Comprehension left baaqi sara ho gaya

## The scope of this project can be expanded to IELTS Preparation as well.

## Test the performance of the different models in OpenAi

        
        ## Also make sure the results generated for word synonnyms, antonyms, might come in a list or maybe not. So write a condition for that in the backend.
        ## Babbage give good results for sentence generation and word meaning. Davinci was the best though.


## Use Google API for translation of small words,and sentences, which is free of cost

## Make the text look more visually appealing. Also, change the Icons, and the UI of the web to make it look more attractive.


## Add the blog post, so that different posts are there.


## Add the contact form, so that the user complains can be listened to.


## Choose a website for deploying. Heroku and Python Anywhere.






## Link for the website from which the contact form was taken. 

## https://learndjango.com/tutorials/django-email-contact-form