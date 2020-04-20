from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')    

def tax_law(request):
    return render(request,'tax-law.html')    

def corporate_law(request):
    return render(request,'corporate-law.html') 