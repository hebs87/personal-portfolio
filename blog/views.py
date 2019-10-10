from django.shortcuts import render


# Create your views here.
def all_blogs(request):
    '''
    Renders the all_blogs.html page and injects
    data from Blog model into the page
    '''
    return render(request, "all_blogs.html")
