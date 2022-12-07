from django.shortcuts import render


def profile(request):
    
    image_url = request.GET.get('/Volumes/Usman/GPT-3 Web Application/media/profile_pics/DALLE_2022-11-04_12.22.24_-_An_image_of_a_lion_and_kangaroo_inside_a_jar_in_iBlyphg.png')
    
    return render(request, 'profile.html', {'image_url': image_url})
