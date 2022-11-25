from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import openai
from googletrans import Translator

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

        text_response = gpt3(text)

        #The context will return the text response

        #By specifying the name of the context in the html, it will display the results.
        
        context = {           
        "htmltext": text_response
    }
       
        return render(request, 'outline_results.html', context)
        
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
        word_meaning= gpt3(f"Write the meaning of {text} in 1. English and 2. Urdu.\n\n")
        
        #return syn
        word_synonym= gpt3(f"Write 3 synonyms of {text}")
        
        #return ant
        word_antonym= gpt3(f"Write 3 antonyms of {text}")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "word_synonym": word_synonym,
        "word_antonym": word_antonym,
        "word_meaning":word_meaning

    }
       
        return render(request, 'synonym.html', context)        
    return render(request, 'synonym.html')



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

    """This function is to make a short summary of a text"""
    
    if request.method == 'POST':
        
        text = request.POST['text']  #The text we will write
        questions= request.POST['questions']
        ## Here, the title will be generated 
        
        #return answers
        answers= gpt3(f"Answer the following questions in the {text}:\n\n + {questions}" ,)
        
     
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "answers": answers,
        

    }
       
        return render(request, 'comprehension.html', context)


        
    return render(request, 'comprehension.html')

####
## Things remaining so far.
####



## Rewrite the sentence without changing the meaning. (include list of how to change)


## Fill in the blank with appropriate words from the options list (general, done!).
## Provide a list in there in which the user can write some words, so that the correct sentence from those words are given. 


#### Translation
#### The translation of GPT-3 is not that good (especially for single sentences), so we have to look for Google translate in this one.


### For short sentences, use Google Translate Api.
### For longer paragraphs, use GPT-3.


### ADD COMPREHENSION
#Very doable!!