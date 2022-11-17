from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import openai

openai.api_key = "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"







# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        print(f"The name {username} has been entered")
        
    return render(request, 'index.html')



def outline(request):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Create outline for topic: Time and tide waits for none\n\n",
    temperature=0.3,
    max_tokens=331,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return HttpResponse(response["choices"][0]["text"])