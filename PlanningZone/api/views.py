from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# all endpoints go here (handler)
# Ex: webpage.com/...
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
#def main(request):
#    return HttpResponse("<h1>hello<h1>")
