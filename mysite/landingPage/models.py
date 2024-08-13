from django.db import models
from django.contrib.auth.models import User
from polls.models import Question, Choice

class UserActionHistory(models.Model):
    ACTION_CHOICES = [
        ('Vote', 'Vote'),
    ]
    
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    action= models.CharField(max_length=20, choices=ACTION_CHOICES)
    timestamp= models.DateTimeField(auto_now_add=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null= True, blank= True)

    def __str__(self):
        return f"{self.user} - {self.action} on {self.question} at {self.timestamp}"
