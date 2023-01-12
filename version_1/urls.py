from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("text-outline", views.outline, name="text_outline"),
    # path("check", views.index),
    path("grammar", views.grammar_correction, name="grammar"),
    path("summary", views.text_summarizer, name="summary"),
    path("sentence", views.word_mean_sentence, name="sentence"),
    path("", views.index, name="home"),
    path("syn_ant", views.syn_anto, name="synonym"),
    path("fill", views.fill_the_blank, name="fillblanks"),
    # path("translate", views.translate, name="translate"),
    path("comprehension", views.comprehension_updated, name="comprehension"),
    path("speech", views.speech_change, name="speech"),
    
    ## This is for contact information
    
    path("contact/", views.contactView, name="contact"),
     path("newcontact/", views.contact_new, name="newcontact"),
    path("success/", views.successView, name="success"),
    path("sessions/", views.attempts_left, name="sessions"),
    path("cache/", views.my_view_cache, name="cache"),


]





## Give prior Prompt examples so that it can pick it up easy, and that the results are good in production.


## Only Comprehension left baaqi sara ho gaya

## The scope of this project can be expanded to IELTS Preparation as well.

## Test the performance of the different models in OpenAi

        
        ## Also make sure the results generated for word synonnyms, antonyms, might come in a list or maybe not. So write a condition for that in the backend.
        ## Babbage give good results for sentence generation and word meaning. Davinci was the best though.


## Use Google API for translation of small words,and sentences, which is free of cost

## Make the text look more visually appealing. Also, change the Icons, and the UI of the web to make it look more attractive.


## Add Recaptcha to cancel bots.



## Add the contact form, so that the user complains can be listened to.


## Choose a website for deploying. Heroku and Python Anywhere.






## Link for the website from which the contact form was taken. 

## https://learndjango.com/tutorials/django-email-contact-form




####
# URGENT WORK TO BE DONE
##

# Integrate it with the latest theme.

# Do one thing. Make a separate template in the main directory so that there is no confusion left.


# I used Google Auth to register new users, and allow them to use services. But I need to check if I can fetch their metadata as well. (Achieved)

# Website used for Google authentication: https://www.codesnail.com/google-authentication-in-django/

######

# BLOGS
###

# About the blog, include the slug, and also the sub title, which will be shown with the blog. And when clicked, the details should be there.
# The slug will be shown in the website.
# Add pagination for the blogs, so that previous blogs can be seen.
# Add keywords on the side, so that blogs relevant to that Keyword are displayed when clicked.
# The blogs should be in descending order (chieved!)
# Also, add pagination in the start, so that things are simple. (Simple is better)

# Good resource : https://www.codesnail.com/django-blog-tutorial/

##### 
# BOOTSTRAP TEMPLATE
####


# Change the theme of the template to make it simple and elegant
# Remove unncessary things.




###
# CONTACT DETAILS
####

# Add it so that users can provide their valuable suggestion about the website.




###
# EMAIL SUBSCRIPTION
### 

# Add a 1 line email subscription so that subsriptions are made. Store it in the data.

