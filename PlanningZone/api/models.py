from django.db import models
import string, random

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if MainPage.objects.filter(roomcode=code).count() == 0:
            break
    return code


# Create your models here.
class Room(models.Model):
    roomcode = models.CharField(max_length=200, default="", unique=True) #code that describes a group session
    host = models.CharField(max_length=50, unique=True) # user that creates the link for everyone

#class User(models.Model):
 #   name = models.CharField(max_length=50, unique=True)
    