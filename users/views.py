from django.shortcuts import render, redirect
from .forms import SubscriberForm, FeedbackForm
from .models import Profile, Subscriber, Feedback

def profile(request):
    
    image_url = request.GET.get('/Volumes/Usman/GPT-3 Web Application/media/profile_pics/DALLE_2022-11-04_12.22.24_-_An_image_of_a_lion_and_kangaroo_inside_a_jar_in_iBlyphg.png')
    
    return render(request, 'profile.html', {'image_url': image_url})





def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        subscriber = Subscriber(email=email)
        subscriber.save()
        return redirect('success')
    return render(request, 'base.html')


def success(request):
    return render(request, 'success.html')


def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        feedback = request.POST['message']
        subscriber = Feedback(name= name, email=email,feedback=feedback, subject=subject )
        subscriber.save()
        return redirect('success')
    return render(request, 'index_2.html')


    
