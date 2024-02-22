from .views import CreateView
from django.urls import path

urlpatterns = [
    path('create',view=CreateView.as_view(),name="Sign-up")
]
