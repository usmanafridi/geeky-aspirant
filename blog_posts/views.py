from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task





def list_mobile(request):

    context= {}

    blogs= Task.objects.all()

    context['blogs']= blogs



    return render(request, 'blog_check.html',context)
