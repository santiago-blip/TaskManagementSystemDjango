from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from apps.user.models import User
from apps.user.serializers.UserSerializer import UserRegisterSerializer
from apps.user.utils import send_email_account_confirmation


import uuid
from dotenv import load_dotenv
import os

class ConfirmationAccountView(APIView):
    def get(self,request,token_email,*args,**kwargs):
        try:
            user = User.objects.get(token_email=token_email) 
            user.is_verified = True
            user.token_email = None
            user.save()
            subject = 'Account confirmed.'
            message = f"Hi {user.username}. \n Thanks for confirming your account."
            send_email_account_confirmation(user,subject,message)
            return Response({"response":"Your account has been verified."},status=status.HTTP_200_OK)
        except:
            return Response({"error":"Token no valid."},status=status.HTTP_404_NOT_FOUND)
    

class GenerateTokenVerification(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        if request.user.is_verified:
            return Response({"error":"Your account is already verified."},status=status.HTTP_400_BAD_REQUEST)
        newToken = uuid.uuid4()
        user = request.user
        user.token_email = newToken
        user.save()
        #EMAIL SETTINGS
        subject = 'Confirmation email'
        BACKEND_URL = os.getenv(f"BACKEND_URL_{os.getenv('ENVIRONMENT')}")
        path = f"{BACKEND_URL}user/confirmation-email/{newToken}"
        message = f"""Hi {user.username}, thank you for registering in task manager. \n
                    click here to confirm your email {path}
        """
        send_email_account_confirmation(user,subject,message)
        return Response({"response":"Your token has been sent."},status=status.HTTP_200_OK)


