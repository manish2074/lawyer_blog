from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class' : 'form-control ggg','placeholder':'Name'}))
    phone = forms.IntegerField(min_value=9000000000,max_value=9999999999,required=True,widget=forms.TextInput(attrs={'class' : 'form-control ggg','placeholder':'Phone no.'}))
    subject = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class' : 'form-control ggg','placeholder':'Subject'}))
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'class' : 'form-control ggg','placeholder':'Your Message Here....'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control ggg','placeholder':'Email'}))
    

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()

   
    
