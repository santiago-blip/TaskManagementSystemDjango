from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import User
from apps.user.serializers.UserSerializer import UserRegisterSerializer
from apps.user.utils import send_email_account_confirmation

from dotenv import load_dotenv
import os

class UserView(APIView):
    def post(self,request):
        data = UserRegisterSerializer(data=request.data)
        # breakpoint()
        data.is_valid(raise_exception=True)
        user = data.save()

        #EMAIL SETTINGS
        subject = 'Confirmation email'
        BACKEND_URL = os.getenv(f"BACKEND_URL_{os.getenv('ENVIRONMENT')}")
        path = f"{BACKEND_URL}user/confirmation-email/{user.token_email}"
        message = f"""Hi {user.username}, thank you for registering in task manager. \n
                    click here to confirm your email {path}
        """
        send_email_account_confirmation(user,subject,message)
        return Response({"response":f"User {user.username} has been created."},status=status.HTTP_201_CREATED)