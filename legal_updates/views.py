from django.shortcuts import render

# Create your views here.
def legal_updates(request):
    return render(request,'legal_updates.html') 