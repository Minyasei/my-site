from django.shortcuts import render, get_object_or_404
from .models import Message

def message_list(request):
    message= Message.objects.all()
    return render(request, 'message_list.html', {'message': message})

def message_detail (request, pk):
    message= get_object_or_404(Message, pk=pk)
    return render (request, 'message_detail.html', {'message':message})

def chat_view(request):
    return render(request, 'chat.html')