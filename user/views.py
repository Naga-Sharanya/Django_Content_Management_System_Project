from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from .serializers import  ForgetPasswordUpdateSerializer, UserLoginSerializer, UserRegistrationSerializer
from user.models import User 
from rest_framework.generics import GenericAPIView


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Successfully Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'tokens': {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    }
                }, status=status.HTTP_200_OK)
            else:
                # Check whether the user exists with the given email
                user_exists = User.objects.filter(email=username).exists()
                if user_exists:
                    # If user exists, password is incorrect
                    return Response({"detail": ("Password is incorrect. Please check it.")}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    # If user doesn't exist, email is incorrect
                    return Response({"detail": ("Email is incorrect. Please check your email.")}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ForgetPasswordUpdateView(APIView):
    def put(self, request):
        serializer = ForgetPasswordUpdateSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']

            try:
                user = User.objects.get(email=email)

                # Reset the password
                user.set_password(new_password)
                user.save()

                return Response({"detail": "Password reset successfully"}, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                return Response({"detail": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


