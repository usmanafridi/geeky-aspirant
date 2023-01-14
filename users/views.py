from django.shortcuts import render, redirect
from .forms import SubscriberForm
from .models import Profile, Subscriber

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

