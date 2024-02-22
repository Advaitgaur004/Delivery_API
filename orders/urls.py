from .views import OrderCreateViewSet,OrderDetailViewSet,OrderListViewSet
from django.urls import path


urlpatterns = [
    path('create/',OrderCreateViewSet.as_view())
]
