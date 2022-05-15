from django.shortcuts import render
from careers.models import Jobs

def index(request):
    jobinstances = Jobs.objects.all()
    context = {
        'jobinstances':jobinstances,
    }
    return render(request, 'pages/index.html',context)
def about(request):
    return render(request, 'pages/about.html')
def adminArea(request):
    return render(request, 'pages/adminarea.html')