from django.shortcuts import render
from rest_framework import generics,status
from .serializers import UserSerializer
from rest_framework.response import Response
import json
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class CreateView(generics.GenericAPIView):
    serializer_class = UserSerializer
    
    @swagger_auto_schema(operation_summary="Register a new user")
    
    def post(self,request):
        data = request.data
        serailizer = UserSerializer(data=data)

        if serailizer.is_valid():
            serailizer.save()
            return Response(data = {"message": "Successfully Registered"},status=status.HTTP_201_CREATED) 
        return Response(data =serailizer.errors , status=status.HTTP_400_BAD_REQUEST)