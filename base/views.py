from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm

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


def room_form(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    context = {
        'form': form    
    }
    return render(request, 'base/room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form    
    }
    return render(request, 'base/room_form.html', context)