from django.shortcuts import render,redirect
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from .forms import ContactForm
# Create your views here.


def contact(request):
   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            subject = f'{subject}-By {name}'
            message_final = f'{message}\n\n Contact Info:\n {phone}'
            send_mail(subject,message_final,email,[EMAIL_HOST_USER],fail_silently=False)
            reply_subject = 'Shraddha Bhattarai - Reply'
            reply_message = f'Dear {name}\n Thank you for reaching me. You will be reached via email or phone within 2-3 business days'
            send_mail(reply_subject,reply_message,EMAIL_HOST_USER,[email],fail_silently=False)
            print(phone)
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})