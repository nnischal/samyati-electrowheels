
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Your Phone Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }
