from django import forms
from django.core.mail import send_mail

class EmailForm(forms.Form):
    initial_email = "oscarchankalung@hotmail.com"

    full_name = forms.CharField(max_length=100, initial="Oscar Chan")
    email = forms.EmailField(max_length=100, initial=initial_email)
    subject = forms.CharField(max_length=100, initial="Subject")
    message = forms.CharField(max_length=100, initial="Test")

    def send_email(self):
        full_name = self.cleaned_data.get("full_name")
        email = self.cleaned_data.get("email")
        subject = self.cleaned_data.get("subject")
        message = self.cleaned_data.get("message")

        content = {
            "subject": f"Email from Django: {subject}",
            "message": f"Name: {full_name}\nEmail: {email}\nMessage: {message}",
            "from": email or self.initial_email,
            "to": [self.initial_email],
        }

        send_mail(
            content["subject"],
            content["message"],
            content["from"],
            content["to"],
            fail_silently=False,
        )
