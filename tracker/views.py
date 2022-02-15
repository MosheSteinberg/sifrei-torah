from django.shortcuts import render
from django.http import HttpResponse

from .models import SeferTorah

# Create your views here.

def index(request):
    return HttpResponse('Hi')
    
def SeforimIndex(request):
    list_of_seforim = [x.id + ": " + x.physical_location for x in SeferTorah.objects.all()]
    return HttpResponse('<br>'.join(list_of_seforim))

def IndividualSefer(request, id):
    
    return HttpResponse('Details of sefer %s here.' % id)