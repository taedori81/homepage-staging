from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #
            recipients = ['taedori@outlook.com']

            send_mail(name, email, message, recipients)
            return HttpResponseRedirect('index.html')
    else:
        form = ContactForm()

    return render(request, "index.html", {'form': form})

