from django.shortcuts import render, get_object_or_404
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


def blog_detail(request, blog_id):
    '''
    Renders the blog_detail.html page and injects
    all blog data into the page - blog_id in the url
    so it needs to be in the relevant function too
    '''
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog_detail': blog_detail,
    }

    return render(request, "blog_detail.html", context)
