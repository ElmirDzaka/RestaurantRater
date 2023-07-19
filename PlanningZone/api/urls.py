from django.contrib import admin
from django.urls import path, include
from .views import RoomView

# store all urls local to api


urlpatterns = [
    path('home', RoomView.as_view()),
]
 