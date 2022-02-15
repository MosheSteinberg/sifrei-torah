from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hi')
    
def SeforimIndex(request):
    return HttpResponse('List seforim here')

def IndividualSefer(request, id):
    return HttpResponse('Details of sefer %s here.' % id)