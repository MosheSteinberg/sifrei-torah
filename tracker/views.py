from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse

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
    sefer = get_object_or_404(SeferTorah, pk=id)
    return render(request, 'tracker/individual_sefer.html', {'sefer':sefer})