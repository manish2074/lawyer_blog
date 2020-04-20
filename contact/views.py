from django.shortcuts import render,redirect
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    if request.method == 'POST':
        print('TJoso')
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        subject = request.POST['subject']
        email = request.POST['email']
        subject = f'{subject}-By {name}'
        message_final = f'{message}\n\n Contact Info:\n {phone}'
        send_mail(subject,message_final,email,['manish.kharel2074@gmail.com'],fail_silently=False)
        print(phone)
        return redirect('home')
    return render(request, 'contact.html')
