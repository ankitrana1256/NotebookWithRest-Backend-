from django.core.mail import EmailMessage
from Notebook3.settings import EMAIL_HOST_USER


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=EMAIL_HOST_USER,
            to=[data['to_email']]
        )
        email.send()