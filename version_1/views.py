from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import openai

openai.api_key = "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"







# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    """This function is written so that I can test how to write post text and get it to the backend of our system"""
    
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        return HttpResponse(f"Hello, {username}. Pleased to meet you.")   
        
    return render(request, 'index.html')





def outline(request):
    """This function is to create outline of a text provided by the user"""
    
    if request.method == 'POST':

        text = request.POST['text']  #The text we will write
        
        response = openai.Completion.create(
        model="text-davinci-002",
        
        prompt=text,
        temperature=0.3,
        max_tokens=331,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        
        text_response = response["choices"][0]["text"]

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
        grammar_sentence = openai.Completion.create(
        model="text-davinci-002",
        
        prompt= f"Correct this to standard English:\n\n + {text}",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )

        #The context will return the grammatically correct sentence
        correct_sentence= grammar_sentence["choices"][0]["text"]
        #By specifying the name of the context in the html, it will display the results.
        
        context = {           
        "correctsentence": correct_sentence
    }
       
        return render(request, 'grammar.html', context)


        
    return render(request, 'grammar.html')