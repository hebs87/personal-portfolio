from django.shortcuts import render
from .models import Job


# Create your views here.
def home(request):
    '''
    Render the home page and inject Job model data
    into the HTML template
    '''
    jobs = Job.objects.all()

    context = {
        "jobs": jobs,
    }

    return render(request, "home.html", context)
