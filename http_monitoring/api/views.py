from django.shortcuts import render
from .serializers import CustomUserSerializer, URLSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request


# Create your views here.

class SignupView(generics.GenericAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data = data)

        if serializer.is_valid():
            serializer.save()
            response = {
                        "message": "User Created Successfully", 
                        "data":serializer.data
                        }
            
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        