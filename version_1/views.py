from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import openai

openai.api_key = "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"


def gpt3(prompt):

    func = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.3,
    max_tokens=700,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    result= func["choices"][0]["text"]
    return result




def index(request):
    """This function is written so that I can test how to write post text and get it to the backend of our system"""
    
        
    return render(request, 'textbox.html')



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
        "correctsentence": text_summary,
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

    """This function is to generate the meaning of word, synonyms and antonyms"""
    
    if request.method == 'POST':
        
        text = request.POST['text']  #The text we will write
 
        #return meaning
        blank_answers= gpt3(f"Fill in the blank with appropriate word:{text}")
        
        #By specifying the name of the context in the html, it will display the results.
        context = {           
        "blank_answers":blank_answers

    }
       
        return render(request, 'blanks.html', context)        
    return render(request, 'blanks.html')



## Rewrite the sentence without changing the meaning.


## Translation