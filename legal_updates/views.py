from django.shortcuts import render
from .models import Events,Legal
from django.shortcuts import get_object_or_404

# Create your views here.
def legal_updates(request):
    legal = Legal.objects.all()[:6]
    events = Events.objects.all()[:6]
    context = {'legal':legal,'events':events}
    return render(request,'legal_updates.html',context) 

def legal_detail(request,slug,pk):
    legal = get_object_or_404(Legal,slug=slug,pk=pk)
    return render(request,'legal_detail.html',{'legal':legal})

def event_detail(request,slug,pk):
    events = get_object_or_404(Events,slug=slug,pk=pk)
    return render(request,'event_detail.html',{'events':events})