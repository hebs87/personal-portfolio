from django.shortcuts import render
from .models import Blog


# Create your views here.
def all_blogs(request):
    '''
    Renders the all_blogs.html page and injects
    data from Blog model into the page
    '''
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, "all_blogs.html", context)
