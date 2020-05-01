from django.shortcuts import render
from .models import Gallery

# Create your views here.
def gallery(request):
    gallery_list = Gallery.objects.all()[:8]
    return render(request,'gallery.html',{'gallery_list':gallery_list}) 