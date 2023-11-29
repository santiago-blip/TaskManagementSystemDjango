from django.urls import path,include
from .views.UserView import UserView
from .views.UserConfirmateAccountView import ConfirmationAccountView,GenerateTokenVerification
from .views.PasswordManagmentView import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', UserView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('confirmation-email/<uuid:token_email>', ConfirmationAccountView.as_view(), name='confirmate_account'),
    path('generate-token-verification',GenerateTokenVerification.as_view()),
    path('confirm-token-password/<uuid:token_password>',ConfirmationAuthenticityPasswordView.as_view()),
    path('generate-token-password',GenerateTokenPassword.as_view()),
    path('reset-password',ResetPassword.as_view())
]