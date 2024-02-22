from django.shortcuts import get_object_or_404
from rest_framework import generics,status 
from rest_framework.response import Response
from .serializer import OrderCreationSerializer,OrderDetailSerializer,OrderUpdateSerializer
from .models import Order
from django.contrib.auth import get_user_model
from .utils import format_date_time
import datetime
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema


User = get_user_model()
# Create your views here.

class OrderCreateViewSet(generics.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="See an Order")
    def get(self,request):
        instance = self.get_queryset()
        serializer =self.serializer_class(instance=instance,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Place an order")
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


class AllOrderDetailViewSet(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="Get all orders")
    def get(self,request):
        instance = self.get_queryset()
        serializer = self.serializer_class(instance=instance,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class OrderDetailViewSet(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated,IsAdminUser]

    @swagger_auto_schema(operation_summary="Get a particular order")
    def get(self,request,**extra_fields):
        order_id = extra_fields['pk']
        order = get_object_or_404(Order,pk = order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data= serializer.data,status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update a particular order")
    def put(self,request,**extra_fields):

        data = request.data
        order_id = extra_fields['pk']
        order = get_object_or_404(Order,pk = order_id)
        serializer = self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data = {"Message":"Successfully changed"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    @swagger_auto_schema(operation_summary="Delete a particular order")   
    def delete(self,request,**extra_fields):
        order_id = extra_fields['pk']
        order = get_object_or_404(Order,pk = order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderUpdateViewSet(generics.GenericAPIView):
    '''
    Update the status of the order
    '''
    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="Update Status of a order")
    def put(self,request,**extra_fields):
        data = request.data
        order_id = extra_fields['pk']
        order = get_object_or_404(Order,pk = order_id)
        serializer = self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data = {"Message":"Successfully changed"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrderViewsets(generics.GenericAPIView):
    '''
    All orders placed by particular Customer
    '''
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Get all orders placed by particular Customer")
    def get(self,request,user_id):
        user = get_object_or_404(User, pk=user_id)
        order = Order.objects.all().filter(customer = user)
        serializer = self.serializer_class(instance=order,many=True) 
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class UserOrderDetails(generics.GenericAPIView):
    '''
    Particular order placed by particular Customer
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OrderDetailSerializer

    @swagger_auto_schema(operation_summary="Get a particular order placed by particular Customer")
    
    def get(self, request, user_id, order_id):
        user = get_object_or_404(User, pk=user_id)
        order = get_object_or_404(Order, pk=order_id, customer=user)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)