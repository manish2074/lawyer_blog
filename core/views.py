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

def error_404_view(request,exception):
    return render(request,'404.html')  

def error_500_view(request):
    return render(request,'500.html')  