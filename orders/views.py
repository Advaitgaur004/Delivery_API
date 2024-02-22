from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .serializer import OrderCreationSerializer
from .models import Order
from .utils import format_date_time
import datetime
from rest_framework.permissions import IsAuthenticated
import os


# Create your views here.

class OrderCreateViewSet(generics.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    def get(self,request):
        instance = self.get_queryset()
        serializer =self.serializer_class(instance=instance,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data = data)
        user = request.user
        if serializer.is_valid():
            serializer.save(customer = user)
            current_date_time = datetime.datetime.now()
            formatted_date_time = format_date_time(current_date_time)
            return Response(data={"Message":"Order Placed", "Created at": f'{formatted_date_time}'},status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class OrderDetailViewSet(generics.GenericAPIView):
    def get(self,request):
        pass
    def post(self,request):
        pass

class OrderListViewSet(generics.GenericAPIView):
    def get(self,request,**extra_fields):
        pass

    def put(self,request,**extra_fields):
        pass

    def delete(self,request,**extra_fields):
        pass

