from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Room, Topic


def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)


def room(request, room_name):
    room = Room.objects.get(link=room_name)
    context = {
        'room_name': room.description,
    }
    return render(request, 'base/room.html', context)
