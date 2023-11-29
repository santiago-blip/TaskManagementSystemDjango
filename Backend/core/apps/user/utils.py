from django.conf import settings
from django.core.mail import send_mail

def send_email_account_confirmation(user,subject,message):

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    send_mail( subject, message, email_from, recipient_list )

def send_email_password_managment(user,subject,message):

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    send_mail( subject, message, email_from, recipient_list )

