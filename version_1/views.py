from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import openai
from googletrans import Translator
from django.template import loader
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit
from django_ratelimit.core import get_usage, is_ratelimited
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.cache import cache
from datetime import datetime, timedelta


import os

openai.api_key = os.environ.get('OPENAI_API_KEY')


#### USE THIS FOR PRECIS AND SUMMARY AS GOOD RESULTS WERE ACHIEVED #####

# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Write precis of the following passage and a suitable title in the end:\n\"Nizar Hassan was born in 1960 and raised in the village of Mashhad, near Nazareth, where he has lived with his\nfamily. He studied anthropology at Haifa University and after graduating worked in TV. Starting in 1990, he\nturned to cinema. In 1994, he produced Independence, in which he pokes his Palestinian interlocutors about what\nthey think of the bizarre Israeli notion of their “independence”. They have stolen another people’s homeland and\ncall the act “independence”! Hassan dwells on that absurdity.\nAs the world’s attention was captured by the news of Israel planning to “annex” yet a bit more of Palestine and\nadd it to what they have already stolen, I received an email from Nizar Hassan, the pre-eminent Palestinian\ndocumentary filmmaker. He wrote to me about his latest film, My Grandfather’s Path, and included a link to the\ndirector’s cut. It was a blessing. They say choose your enemies carefully for you would end up like them. The\nsame goes for those opposing Zionist settler colonialists. If you are too incensed and angered by their daily dose of\nclaptrap, the vulgarity of their armed robbery of Palestine, you would soon become like them and forget yourself\nand what beautiful ideas, ideals, and aspirations once animated your highest dreams. Never fall into that trap. For\ndecades, aspects of Palestinian and world cinema, art, poetry, fiction, and drama have done for me precisely that:\nsaved me from that trap. They have constantly reminded me what all our politics are about – a moment of poetic\nsalvation from it all.\nNizar Hassan’s new documentary is one such work – in a moment of dejection over Israel’s encroachment on\nPalestinian rights and the world’s complicity, it has put Palestine in perspective. The film is mercifully long,\nbeautifully paced and patient, a masterfully crafted work of art – a Palestinian’s epic ode to his homeland. A\nshorter version of My Grandfather’s Path has been broadcast on Al Jazeera Arabic in three parts, but it must be\nseen in its entirety, in one go. It is a pilgrimage that must not be interrupted. \"\n\n\nNizar Hassan, a Palestinian documentary filmmaker born in 1960, produced the film 'Independence', wherein he pokes his Palestinian interlocutors about Israel's bizarre notion of \"independence\". His latest work, 'My Grandfather's Path' is an epic ode to his homeland that should be seen in its entirety. It captures a moment of poetic salvation from the clutches of Israeli encroachment and world complicity while reminding us what all our politics are about. \nTitle: Nizar Hassan’s ‘My Grandfather’s Path’ - An Epic Ode To Palestine",
#   temperature=0.7,
#   max_tokens=1002,
#   top_p=1,
#   frequency_penalty=2,
#   presence_penalty=0.28
# )

############################################



##### USE THIS FOR WORD MEANING AS GOOD RESULTS WERE ACHIEVED:

# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-curie-001",
#   prompt="The meaning of \"Islamophobic\".\n\n\n\nIslamophobic is a term used to describe a person who is afraid or hostile towards Muslims.",
#   temperature=0.1,
#   max_tokens=25,
#   top_p=1,
#   frequency_penalty=0.18,
#   presence_penalty=0
# )

################################################


########## FOR SYNONYMS AND ANTONYMS MINIMAL ########

# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-curie-001",
#   prompt="Write antonyms of \"Pejorative\".\n\n\n\nAffectionate, endearing, complimentary, kind, positive",
#   temperature=0.1,
#   max_tokens=25,
#   top_p=1,
#   frequency_penalty=0.27,
#   presence_penalty=0
# )

######################################################

## Helper function for Cache counter.
def cache_counter(request, turns_remaing = 3 ):
    key = f"user:{request.user.id}"
    remaining = cache.get(key)
    if remaining is None:
        remaining = turns_remaing
    else:
        remaining -= 1
    cache.set(key, remaining)
    return remaining


### Using Cache
def my_view_cache(request):
    
    remaining= cache_counter(request, turns_remain= 5 )
    return render(request, 'my_template.html', {'attempts_left': remaining})


def check_bootstrap(request):
    
    return render(request, 'login_good.html')



## This is to handle the sessions and give the user about how many times he can access the web page. But it is for the overall pages.
def attempts_left(request):
    session = request.session
    if 'page_counter' not in session:
        session['page_counter'] = 0
    session['page_counter'] += 1
    if session['page_counter'] > 3:
        return redirect('outline.html')
    else:
        attempts_left = 3 - session['page_counter']
        return render(request, 'my_template.html', {'attempts_left': attempts_left})


def gpt3(prompt, tokens=900, temperature=0.7, presence=0.23):
    func = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=temperature,
    max_tokens=tokens,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=presence
    )
    result= func["choices"][0]["text"]
    return result





def index(request):
    """This function is written so that I can test how to write post text and get it to the backend of our system"""
    return render(request, 'index_2.html')


@ratelimit(key='ip', rate='5/d')
def outline(request):
    """This function is to create outline of a text provided by the user"""
    
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write (Here the "text" is the name of the form in html )
        words= int(request.POST['vol'])
        if len(text) >= 200:
            text = "Access limit has been reached. Please reduce words. The max number of words are ...."
            text_response= ''
        else:
            text= text
            text_response = gpt3(f"Write an outline of {text},  ", tokens=words)
        
        ## Here, we can add more functionality in the premium package as we can increase number of Tokens to make it more detailed.
        
        
        #The context will return the text response
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "htmltext": text_response,
        "text":text
    }
        return render(request, 'outline.html', context)
    return render(request, 'outline.html')

@ratelimit(key='ip', rate='50/d')
def grammar_correction(request):
    """This function is to correct any grammatical mistake in a sentence"""
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
        if len(text) >= 200:
            text = "Access limit has been reached. Please reduce words. The max number of words are ...."
            correct_sentence= None
        else:
            text= text
        #The context will return the grammatically correct sentence
            correct_sentence= gpt3(f"Correct this {text} to standard English: ")
        #By specifying the name of the context in the html, it will display the results.
        print(text)
        context = {           
        "correctsentence": correct_sentence,
        "text": text
    }
       
        return render(request, 'grammar.html', context)
    return render(request, 'grammar.html')

@ratelimit(key='ip', rate='5/d')
def text_summarizer(request):
    """This function is to make a short summary of a text"""
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
        if len(text) >= 2500:
            text = "Access limit has been reached. Please reduce words. The max number of words are ...."
            text_summary= None
        else:
            text= text
        ##return summary
            text_summary= gpt3(f"Write precis of the following passage and a suitable title in the end\n\n + {text}")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "correctsummary": text_summary,
        "text":text
    }
        return render(request, 'summary.html', context)
    return render(request, 'summary.html')


@ratelimit(key='ip', rate='15/d')
def text_paraphraser(request):
    """This function is to make a short paraphraser of a text"""
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
        if len(text) >= 2500:
            text = "Access limit has been reached. Please reduce words. The max number of words are ...."
            text_paraphrase= None
        else:
            text= text
        ##return summary
            text_paraphrase= gpt3(f"Paraphrase {text}\n")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "text_paraphrase": text_paraphrase,
        "text":text
    }
        return render(request, 'paraphrase.html', context)
    return render(request, 'paraphrase.html')



def word_mean_sentence(request):
    """This function is to make sentences and write the meaning of the words"""
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
        ## Here, the title will be generated  
        #return title
        
        
        
        
        word_meaning= gpt3(f"Write the meaning of {text} in English\n\n")
        #return sentence
        word_sentence= gpt3(f"Use {text} in a sentence")

        
        
        
        
        translated_text= translator = Translator()
        translations= translator.translate(text, dest= ln)
        translation= translations.text
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "word_meaning": word_meaning,
        "word_sentence": word_sentence,
        "text":text
    }       
        return render(request, 'sentences.html', context)
    return render(request, 'sentences.html')

@ratelimit(key='ip', rate='5/d')
def syn_anto(request):
    """This function is to generate the meaning of word, synonyms and antonyms"""
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
        if len(text)>= 100:
            text= "The text contains too many words"
            word_meaning=None
            word_synonym= None
            word_antonym= None
            print(text)
        else:
            text=text
            print(text)
        #return meaning
            word_meaning= gpt3(f"Write the meaning of {text} \n\n")
            #return syn
            word_synonym= gpt3(f"Write at least three synonyms of {text} \n\n")
            #return ant
            word_antonym= gpt3(f"Write at least three antonyms of {text}\n\n ")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "word_synonym": word_synonym,
        "word_antonym": word_antonym,
        "word_meaning":word_meaning,
        "text":text
    }
        return render(request, 'synonym.html', context)        
    return render(request, 'synonym.html')



## In fill in the blanks, give prior examples so that the prompt can pick this up.
@ratelimit(key='ip', rate='15/d')
def fill_the_blank(request):
    """This function is to return words in the blanks provided in the sentence."""
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
        if len(text)>= 100:
            text= "The text contains too many words"
            blank_answers=None
            print(text)
        
        else:
            text=text
            print(text)
        #return words in the blanks
            blank_answers= gpt3(f"Fill in the blank with appropriate word: \n{text}")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "blank_answers":blank_answers,
        "text":text
    }
        return render(request, 'blanks.html', context)        
    return render(request, 'blanks.html')

# @ratelimit(key='ip', rate='5/m')
# def translate(request):

#     """This function is to translate the text provided to it. We will use Google translate API in this one. But one thing must be kept in mind that the 
#     translation of GPT-3 is not that accurate, comparatively, that of Google is better. """
   
   
#     if request.method == 'POST':
#         remaining= cache_counter(request, turns_remaing = 3 )
#         text = request.POST['text']  #The text we will write
#         vol = request.POST['vol']
#         print(vol)
#         lang_type = request.POST.get('lang')
#         if lang_type == 'Urdu':
#             lang="Urdu" 
#             ln="ur"
                
#         elif lang_type == 'English':
#             lang="English"
#             ln="en" 

#         else:
#             lang="Hindi"
#             ln="hi"
            
        
#         #return the translation in Google.
#         if len(text) > 150:

#             translation= gpt3(f"Translate the following text in {lang}: \n\n {text} ")
#             print("Translation using GPT-3")
        
#         else:
#             translator = Translator()
#             translations= translator.translate(text, dest= ln)
#             translation= translations.text
#         #By specifying the name of the context in the html, it will display the results.
#             print("Translated using Googel api")
        
        
#         context = {           
        
#         "translation":translation,
#         "text":text,
#         'attempts_left': remaining,
        
#     }
#         return render(request, 'translation.html', context)        
    
    
    
    
#     return render(request, 'translation.html')
    
    
    


@ratelimit(key='ip', rate='5/d')
def comprehension(request):

    
    ## This is to calcualte the number of requests made so that the questions can be answered dynamically!!
    post_data = request.POST

    # Get the number of textboxes that were created
    num_textboxes = len(post_data)

    print(f"The number of post request: {num_textboxes}")

    print(f"Post data is { post_data.items()}")

    """This function is to write comprehension answers of a text"""
    
    statement= """Answer the questions from the following passage and do not 
    include infromation or examples which is not mentioned in the passage """
    
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
        print(len(text))
        if len(text)>= 15000:
            text= "The passage is too big, please reduce size"
            answers=None
            print(text)
        else:
            text=text
            print(text)
        
            if num_textboxes > 0 and num_textboxes <= 3:
                question1= '1.' + request.POST['textbox1']
                #return answers
                answers= gpt3(f"Answer the questions from \n\{text}.\ \nQuestions:\n \n{question1}\n\nAnswer:\n"  )
            
            elif num_textboxes > 3 and num_textboxes <= 4:
                question1= '1.' + request.POST['textbox1']
                question2= '2.' + request.POST['textbox2']
                answers= gpt3(f"Answer the questions from \n\{text}.\ \nQuestions:\n \n{question1}\n {question2}\nAnswer:\n" )

            elif num_textboxes > 4 and num_textboxes <= 5:
                question1= '1.' + request.POST['textbox1']
                question2= '2.' + request.POST['textbox2']
                question3= '3.' + request.POST['textbox3']
                answers= gpt3(f"Answer the questions from \n\{text}.\ \nQuestions:\n \n{question1}\n {question2}\n {question3}\nAnswer:\n" )

            elif num_textboxes > 5 and num_textboxes <= 6:
                question1= '1.' + request.POST['textbox1']
                question2= '2.' + request.POST['textbox2']
                question3= '3.' + request.POST['textbox3']
                question4= '4.' + request.POST['textbox4']
                answers= gpt3(f"Answer the questions from \n\{text}.\ \nQuestions:\n \n{question1}\n {question2}\n {question3}\n {question4}\nAnswer:\n" )

            elif num_textboxes > 6 and num_textboxes <= 7:

                question1= '1.' + request.POST['textbox1']
                question2= '2.' + request.POST['textbox2']
                question3= '3.' + request.POST['textbox3']
                question4= '4.' + request.POST['textbox4']
                question5= '5.' + request.POST['textbox5']
                answers= gpt3(f"Answer the questions from \n\{text}.\ \nQuestions:\n \n{question1}\n {question2}\n {question3}\n {question4}\n {question5}\nAnswer:\n" )

            else:
                None
        context = {           
        "answers": answers,
        "text" :text }
    
        return render(request, 'comprehension.html', context)
    return render(request, 'comprehension.html')



## This function will be called when the rate limit is exceeded,
def rate_limit_reached(request, exception):
    return render(request, 'rate.html')


### The comprehension questions can be dealt in two ways. 
  ## One way is to ask the questions from a given passage.
  ## Another one is to fill in the blanks.
  ## The updated one, I have included to incude fill in the blanks, the above when is for questions.
  ## But a great care must be taken in the Prompt selection, as everything depends on that.

@ratelimit(key='ip', rate='20/d')
def punctuation(request):

    if request.method == 'POST': 
        text = request.POST['text']  #The text we will write
        #return words in the blanks
        answers= gpt3(f"Put in comma, semicolons, colons, dashes, hyphen, quotation marks, question mark, exclamation point, and brackets where neede in {text}\n" )
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "punctuation":answers,
        "text":text
    }
        return render(request, 'punctuation.html', context)  
        # Check if the rate limit has been reache
    return render(request, 'punctuation.html')



### NOT USED SO FAR.
@ratelimit(key='ip', rate='100/m')
def comprehension_updated(request):

    if request.method == 'POST': 
        text = request.POST['text']  #The text we will write

        #return words in the blanks
        questions= request.POST['textbox_question']

        answers= gpt3(f"Fill the blank in {questions} from the {text} " )
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        
        "answers":answers
    }
        return render(request, 'comprehension.html', context)  
    
        # Check if the rate limit has been reache
    
    
    return render(request, 'comprehension.html')


@ratelimit(key='ip', rate='20/d')   
@login_required(redirect_field_name='speech')
def speech_change(request):

    """This function is to change the speech into direct and indirect """
    
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write

        speech_type = request.POST.get('speech')

        if speech_type == 'direct':
            speech="Direct Speech" 
            

        else:
            speech="Indirect Speech" 
           
        speech_change= gpt3(f"Change {text} into {speech}:\n")
    
        context = {           
        
        "speech_result":speech_change,
        "text":text
    }
        return render(request, 'direct_indirect.html', context)        
    return render(request, 'direct_indirect.html')

        


def contact_new(request):

    """This is contact for demo purpose """
    
    if request.method == 'POST':
        
        name= request.POST['name'] 
        email= request.POST['email'] 
        subject= request.POST['subject'] 
        
        text = request.POST['message']  #The text we will write


           
        final_message= gpt3(f"{text} ")
    
        context = {           
        "name": name,
        "email": email,
        "subject":subject,
        "text":text,
        "final_message": final_message
    }
        return render(request, 'new_contact.html', context)        
    return render(request, 'new_contact.html')




def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            try:
                send_mail(subject, message, name, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success") #This redirect to the success page after successful contact post.
    
    return render(request, "contact.html", {"form": form})

def successView(request):
    return render(request, "success.html")








#### Functionality Remaining:

## Give the user the option to upload the file so the text can be copied from it. 

## Give another funtionality in which the user can copy the result and paste it in the word



####
## Things remaining so far.
####


## The chucks can be made. This week, try to visually make the app good. And in parallel, use Google auth, and pricing mechanism as well.

## Use a simple login authentication where the user can just enter their email, and then, they can access all the features of the website.

## Use ReCaptcha so that bots are not able to enter into the website. Because then the API will be completely lost.




## Remove p-2 from the text area box so that the texts are aligned in the input and output box.

## In the fill in the blanks section, give the user the choice of how he/she wants to fill the blank.

## Rewrite the sentence without changing the meaning. (include list of how to change)


## Fill in the blank with appropriate words from the options list (general, done!).
## Provide a list in there in which the user can write some words, so that the correct sentence from those words are given. 


#### Translation
#### The translation of GPT-3 is not that good (especially for single sentences), so we have to look for Google translate in this one.


### For short sentences, use Google Translate Api.
### For longer paragraphs, use GPT-3.



## Add a dialogue between two friends.

## Tense correction.

## Prepositions

## Conjunctions