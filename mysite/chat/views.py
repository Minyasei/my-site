from django.shortcuts import render, redirect
from .models import Room, Message

def home(request):
    return render(request, 'chat/home.html')

def room(request, room_name, username):
    context = {'room_name': room_name, 'username': username}
    return render(request, 'chat/room.html', context)

def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']
    
    if Room.objects.filter(name=room_name).exists():
        return redirect(f'/{room_name}/username={username}')
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect(f'/{room_name}/username={username}')
