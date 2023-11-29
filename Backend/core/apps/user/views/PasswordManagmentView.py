from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from apps.user.models import User
from apps.user.serializers.UserSerializer import UserRegisterSerializer
from apps.user.utils import send_email_password_managment
from apps.user.serializers.PasswordResetSerializer import ValidatePassword

import uuid
from dotenv import load_dotenv
import os

class ConfirmationAuthenticityPasswordView(APIView):
    def get(self,request,token_password=None,*args,**kwargs):
        try:
            user = User.objects.get(token_password_recover=token_password) 
            return Response({"response":"The token is valid."},status=status.HTTP_200_OK)
        except:
            return Response({"error":"Token no valid."},status=status.HTTP_404_NOT_FOUND)
    

class GenerateTokenPassword(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):

        newToken = uuid.uuid4()
        user = request.user
        user.token_password_recover = newToken
        user.save()
        #EMAIL SETTINGS
        subject = 'Password recovery token'
        message = f"""Hi {user.username}, this is your password recovery token: \n
                    {newToken}
        """
        send_email_password_managment(user,subject,message)
        return Response({"response":f"Your token has been sent to your email. token: \
                         {newToken}"},status=status.HTTP_200_OK)

class ResetPassword(APIView):
    def post(self,request,*args,**kwargs):
        try:
            user = User.objects.get(token_password_recover=request.data.get('token_password_recover'))
        except:
            return Response({"error":"Token no valid."},status=status.HTTP_404_NOT_FOUND)

        data = ValidatePassword(data=request.data)
        data.is_valid(raise_exception=True)
        # breakpoint()
        # user.set_password(data.validated_data['password'])
        user.token_password_recover = None
        user.save()
        subject = 'Password reset'
        message = f"""Hi {user.username}, your password has been reset"""
        send_email_password_managment(user,subject,message)
        return Response({"response":"The password has been changed."},status=status.HTTP_200_OK)
