from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=20, unique=True)

class Message(models.Model):
    value = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=30)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
