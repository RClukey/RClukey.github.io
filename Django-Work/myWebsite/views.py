from django.shortcuts import render
from bakery.views import BuildableDetailView, BuildableListView

from .models import MetalEarth, Picture

# Create your views here.

def index(request):
    return render(request, 'myWebsite/index.html')

def metalearth(request):
    metalearths = MetalEarth.objects.all()
    
    return render(request, 'myWebsite/metalearth.html', {
        'metalearths': metalearths,
    })

def resume(request):
    return render(request, 'myWebsite/resume.html')

def sculpture(request, name):
    sculp = MetalEarth.objects.get(name=name)

    return render(request, 'myWebsite/metalearth.html', {
        'sculpture': sculp,
    })

def youtube(request):
    return render(request, 'myWebsite/youtube.html')

def viewPDF(request, viewer):
    return render(request, 'myWebsite/PDFviewer.html', {
        'viewer': viewer,
    })