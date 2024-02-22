from .views import AllOrderDetailViewSet,OrderCreateViewSet,OrderDetailViewSet,OrderUpdateViewSet,UserOrderViewsets,UserOrderDetails
from django.urls import path


urlpatterns = [
    path('create/',OrderCreateViewSet.as_view()),
    path('detail/',AllOrderDetailViewSet.as_view()),
    path('detail/<int:pk>/',OrderDetailViewSet.as_view()),
    path('update/<int:pk>/',OrderUpdateViewSet.as_view()),
    path('user/<int:user_id>/orders/',UserOrderViewsets.as_view()),
    path('user/<int:user_id>/orders/<int:order_id>/',UserOrderDetails.as_view()),
]
