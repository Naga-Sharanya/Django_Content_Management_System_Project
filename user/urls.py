from .views import  ForgetPasswordUpdateView, UserRegistrationView,UserLoginView
from django.urls import path
# from .views import ForgotPasswordView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('reset-password/', ForgetPasswordUpdateView.as_view(), name='reset-password'),

]