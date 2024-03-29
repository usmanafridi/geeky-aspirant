from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task





def list_mobile(request):

    context= {}

    
    blogs= Task.objects.order_by('-date_posted')

    context['blogs']= blogs



    return render(request, 'index_blog.html',context)

    ## Here, when passing the template name, it will detect it from anyhere. Case sensitive


def retrieve_blog(request, id):
    # filter
    # get_or_404
    # error handling
    blog= get_object_or_404(Task, id=id)
    context = {
        'blog': blog
    }
    return render(request, 'detail.html', context)


## Good website for blog creation : https://justdjango.com/blog/build-a-blog-with-django