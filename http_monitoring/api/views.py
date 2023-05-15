from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import CustomUserSerializer, UrlSerializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request


# Create your views here.

# Here we handel Sign up requests
class SignupView(generics.GenericAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request: Request):
        print('in sign up view - post method')
        data = request.data

        serializer = self.serializer_class(data = data)

        if serializer.is_valid():
            print('in sign up view - if statement 1')
            serializer.save()
            print('in sign up view - if statement 2')
            response = {
                        "message": "User Created Successfully", 
                        "data":serializer.data
                        }
            
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Here we handel Log in requests and authentications with Tokens
class LoginView(APIView):
    
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        # This method is checking if the user have a Token
        user = authenticate(email=email, password=password)

        if user is not None:
            response = {
                'message': 'Login Successful',
                'token': user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)

    def get(self, request: Request):

        response = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=response, status=status.HTTP_200_OK)