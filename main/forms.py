
from django import forms
from parsley.decorators import parsleyfy


@parsleyfy
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Your Name'}), label='Name', max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Messages'}))


