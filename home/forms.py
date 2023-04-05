from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['fname', 'lname', 'email', 'comment']
        widgets = {
            'fname': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'First Name'
                }),
            'lname': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Last Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'width: 100%;',
                'placeholder': 'Email'
                }),
            'comment': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Message'
                }),
        }
