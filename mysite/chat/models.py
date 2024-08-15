from django.db import models

class User(models.Model):
    name= models.CharField(max_length=140)
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name="recieved_mesage")
    subject= models.CharField(max_length= 200)
    body= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    