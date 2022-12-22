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

openai.api_key = "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"


def gpt3(prompt):

    func = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.3,
    max_tokens=900,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    result= func["choices"][0]["text"]
    return result


def index(request):
    """This function is written so that I can test how to write post text and get it to the backend of our system"""
    
        
    return render(request, 'index.html')


def outline(request):
    """This function is to create outline of a text provided by the user"""
    
    if request.method == 'POST':

        text = request.POST['text']  #The text we will write (Here the "text" is the name of the form in html )

        text_response = gpt3(f"Write 10 outlines of {text} ")

        #The context will return the text response

        #By specifying the name of the context in the html, it will display the results.
        
        context = {           
        "htmltext": text_response
    }
       
        return render(request, 'outline.html', context)
        
    return render(request, 'outline.html')


def grammar_correction(request):
    """This function is to correct any grammatical mistake in a sentence"""
    
    if request.method == 'POST':
        
        text = request.POST['text']  #The text we will write
       
        #The context will return the grammatically correct sentence
        correct_sentence= gpt3(f"Correct this to standard English:\n\n + {text}")
        #By specifying the name of the context in the html, it will display the results.
        
        context = {           
        "correctsentence": correct_sentence
    }
       
        return render(request, 'grammar.html', context)
    return render(request, 'grammar.html')


def text_summarizer(request):

    """This function is to make a short summary of a text"""
    
    if request.method == 'POST':
        
        text = request.POST['text']  #The text we will write

        ## Here, the title will be generated 
        #return title
        title= gpt3(f"Suggest a title for the following passage\n\n + {text}")
        
        #return summary
        text_summary= gpt3(f"{text}+\n\nTl;dr",)
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "correctsummary": text_summary,
        "correcttitle": title,

    }
       
        return render(request, 'summary.html', context)


        
    return render(request, 'summary.html')


def word_mean_sentence(request):

    """This function is to make sentences and write the meaning of the words"""
    
    if request.method == 'POST':
        
        text = request.POST['text']  #The text we will write
        ## Here, the title will be generated  
        
        #return title
        word_meaning= gpt3(f"Write the meaning of {text} in English\n\n")
        
        #return sentence
        word_sentence= gpt3(f"Use {text} in a sentence")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "word_meaning": word_meaning,
        "word_sentence": word_sentence,
    }       
        return render(request, 'sentences.html', context)
    return render(request, 'sentences.html')


def syn_anto(request):

    """This function is to generate the meaning of word, synonyms and antonyms"""
    
    if request.method == 'POST':
        
        text = request.POST['text']  #The text we will write
 
        #return meaning
        word_meaning= gpt3(f"Write the meaning of {text} \n\n")
        
        #return syn
        word_synonym= gpt3(f"Write at least three synonyms of {text} \n\n")
        
        #return ant
        word_antonym= gpt3(f"Write at least three antonyms of {text}\n\n ")

        word_sentence= gpt3(f"Use {text} in a sentence")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "word_synonym": word_synonym,
        "word_antonym": word_antonym,
        "word_meaning":word_meaning,
       

    }
       
        return render(request, 'synonym.html', context)        
    return render(request, 'synonym.html')



## In fill in the blanks, give prior examples so that the prompt can pick this up.

def fill_the_blank(request):

    """This function is to return words in the blanks provided in the sentence."""
    
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
 
        #return words in the blanks
        blank_answers= gpt3(f"Fill in the blank with appropriate word:{text}")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        
        "blank_answers":blank_answers
    }
        return render(request, 'blanks.html', context)        
    return render(request, 'blanks.html')


def translate(request):

    """This function is to translate the text provided to it. We will use Google translate API in this one. But one thing must be kept in mind that the 
    translation of GPT-3 is not that accurate, comparatively, that of Google is better. """
    
  

    
    
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write
        
        vol = request.POST['vol']
        print(vol)
        
        
        lang_type = request.POST.get('lang')

        if lang_type == 'Urdu':
            lang="Urdu" 
            ln="ur"
                
        elif lang_type == 'English':
            lang="English"
            ln="en" 

        else:
            lang="Hindi"
            ln="hi"
            
        
        #return the translation in Google.
        if len(text) > 150:

            translation= gpt3(f"Translate the following text in {lang}: \n\n {text} ")
            print("Translation using GPT-3")
        
        else:
            translator = Translator()
            translations= translator.translate(text, dest= ln)
            translation= translations.text
        #By specifying the name of the context in the html, it will display the results.
            print("Translated using Googel api")
        
        
        context = {           
        
        "translation":translation
    }
        return render(request, 'translation.html', context)        
    return render(request, 'translation.html')



def comprehension(request):

    
    ## This is to calcualte the number of requests made so that the questions can be answered dynamically!!
    post_data = request.POST

    # Get the number of textboxes that were created
    num_textboxes = len(post_data)

    print(f"The number of post request: {num_textboxes}")

    print(f"Post data is { post_data.items()}")

    """This function is to write comprehension answers of a text"""
    
    if num_textboxes > 0 and num_textboxes <= 4:
        if request.method == 'POST':
            text = request.POST['text']  #The text we will write
            
            question1= request.POST['textbox1']
            # question2= request.POST['textbox2']
            #Here the answers will be generated.
        
            #return answers
            answers= gpt3(f"Answer the following questions in the {text}: + {question1} +\n\n " )
            context = {           
        "answers": answers}
       
        return render(request, 'comprehension.html', context)
    
    elif num_textboxes > 4 and num_textboxes <= 5:
        
        if request.method == 'POST':
            d={}
            text = request.POST['text']  #The text we will write
            
            question1= request.POST['textbox1']
            question2= request.POST['textbox2']

        
            #Here the answers will be generated.
            

            #return answers
            answers= gpt3(f"Answer the following questions in the {text}: + {question1} +\n\n {question2} " )
            
            context = {           
        "answers": answers}
       
        return render(request, 'comprehension.html', context)

    elif num_textboxes > 5 and num_textboxes <= 6:
        
        if request.method == 'POST':
            d={}
            text = request.POST['text']  #The text we will write
            
            question1= request.POST['textbox1']
            question2= request.POST['textbox2']
            question3= request.POST['textbox3']

        
            #Here the answers will be generated.
            

            #return answers
            answers= gpt3(f"Answer the following questions in the {text}: + {question1} +\n\n {question2} +\n\n {question3}" )
            
            context = {           
        "answers": answers}
       
        return render(request, 'comprehension.html', context)



    elif num_textboxes > 6 and num_textboxes <= 7:
        
        if request.method == 'POST':
            d={}
            text = request.POST['text']  #The text we will write
            
            question1= request.POST['textbox1']
            question2= request.POST['textbox2']
            question3= request.POST['textbox3']
            question4= request.POST['textbox4']

        
            #Here the answers will be generated.
            

            #return answers
            answers= gpt3(f"Answer the following questions in the {text}: + {question1} +\n\n {question2} +\n\n {question3}+\n\n {question4}" )
            
            context = {           
        "answers": answers}
       
        return render(request, 'comprehension.html', context)

    elif num_textboxes > 7 and num_textboxes <= 8:
        
        if request.method == 'POST':
            d={}
            text = request.POST['text']  #The text we will write
            
            question1= request.POST['textbox1']
            question2= request.POST['textbox2']
            question3= request.POST['textbox3']
            question4= request.POST['textbox4']
            question5= request.POST['textbox5']

        
            #Here the answers will be generated.
            

            #return answers
            answers= gpt3(f"Answer the following questions in the {text}: + {question1} +\n\n {question2} +\n\n {question3}+\n\n {question4}+\n\n {question5}" )
            
            context = {           
        "answers": answers}
       
        return render(request, 'comprehension.html', context)

    
    else:
        None
        
        #By specifying the name of the context in the html, it will display the results.
        
       
        
        


        
    return render(request, 'comprehension.html')



### The comprehension questions can be dealt in two ways. 
  ## One way is to ask the questions from a given passage.
  ## Another one is to fill in the blanks.
  ## The updated one, I have included to incude fill in the blanks, the above when is for questions.
  ## But a great care must be taken in the Prompt selection, as everything depends on that.

@ratelimit(key='ip', rate='4/m')
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
    
    
    
    return render(request, 'comprehension.html')

    

def speech_change(request):

    """This function is to change the speech into direct and indirect """
    
    if request.method == 'POST':
        text = request.POST['text']  #The text we will write

        speech_type = request.POST.get('speech')

        if speech_type == 'direct':
            speech="Direct Speech" 
            

        else:
            speech="Indirect Speech" 
           
        speech_change= gpt3(f"Change the following into {speech}: \n\n {text} ")
    
        context = {           
        
        "speech_result":speech_change
    }
        return render(request, 'direct_indirect.html', context)        
    return render(request, 'direct_indirect.html')

        





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
    return HttpResponse("Success! Thank you for your message.")



#### Functionality Remaining:

## Give the user the option to upload the file so the text can be copied from it. 

## Give another funtionality in which the user can copy the result and paste it in the word



####
## Things remaining so far.
####



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