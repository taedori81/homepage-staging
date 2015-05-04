from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm

# TODO
# Change to Class-based views


# def home(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             from_email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#
#             recipients = ['taedori@outlook.com']
#             subject = "Message from " + name
#
#             mail = EmailMessage(subject, message, from_email, recipients)
#             mail.send()
#
#     else:
#         form = ContactForm()
#
#     return render(request, "index.html", {'form': form})


class HomepageView(TemplateView):

    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['taedori@outlook.com']
            subject = "Message from " + name

            mail = EmailMessage(subject, message, from_email, recipients)
            mail.send()

            form = ContactForm()

        return render(request, self.template_name, {'form': form})
















