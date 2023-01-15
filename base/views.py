from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from .models import Room, Topic, User
from .forms import RoomForm

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username or password is incorrect')
            print('user does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {

    }
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    q = request.GET.get('q')
    if q:
        # get all the rooms that have a topic that contains the query
        rooms = Room.objects.filter(
            Q(topics__name__icontains=q) |
            Q(topics__description__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q)
        ).distinct(
            # order by the number of topics that match the query
        )
    else:
        # get all the rooms
        rooms = Room.objects.all()
    topics = Topic.objects.all()
    context = {
        'rooms': rooms,
        'topics': topics
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


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {
        'item': room
    }
    return render(request, 'base/delete.html', context)
