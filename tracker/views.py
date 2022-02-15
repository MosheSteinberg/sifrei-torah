from django.shortcuts import render
from django.http import HttpResponse

from .models import SeferTorah

# Create your views here.

def index(request):
    return HttpResponse('Hi')
    
def SeforimIndex(request):
    context = {
        'seforim': SeferTorah.objects.all()
    }
    return render(request, 'tracker/seforim_index.html', context)

def IndividualSefer(request, id):
    
    return HttpResponse('Details of sefer %s here.' % id)