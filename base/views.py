from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from .models import Room, Topic, User, Message
from .forms import RoomForm, UserForm


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
        'title': 'Login'
    }
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

# class Room(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200, null=True, blank=True)
#     link = models.CharField(max_length=50)
#     # delete the room when the last topic it belongs to is deleted
#     topics = models.ManyToManyField('Topic', related_name='rooms', blank=True)
#     participants = models.ManyToManyField(
#         User, related_name='rooms_joined', blank=True)
#     host = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='rooms_hosted')
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['-updated', '-created']


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.rooms_hosted.all() | user.rooms_joined.all()
    topics = Topic.objects.filter(rooms__in=rooms)
    recent_messages = Message.objects.filter(
        user=user).order_by('-created')[:5]
    context = {
        "profuser": user,
        "rooms": rooms,
        "topics": topics,
        "recent_messages": recent_messages,
    }
    return render(request, 'base/profile.html', context)


def registerPage(request):
    context = {
        'title': 'Register',
        'form': UserCreationForm,
    }
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request, 'An error has occurred during registration')
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q')
    if q:
        # get all the rooms that have a topic that contains the query
        rooms = Room.objects.filter(
            Q(topics__name__icontains=q) |
            Q(topics__description__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q)
        ).distinct()
        recent_messages = Message.objects.filter(
            Q(room__topics__name__icontains=q) |
            Q(room__topics__description__icontains=q) |
            Q(room__name__icontains=q) |
            Q(room__description__icontains=q) |
            Q(message__icontains=q)
        ).distinct().order_by('-created')[:5]
    else:
        # get all the rooms
        rooms = Room.objects.all()
        recent_messages = Message.objects.all().order_by('-created')[:5]
    topics = Topic.objects.all()
    context = {
        'rooms': rooms,
        'topics': topics,
        'recent_messages': recent_messages,
    }
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(link=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Message.objects.create(
                user=request.user,
                room=room,
                message=message
            )
            room.participants.add(request.user)
            room.save()
            return redirect('room', pk=pk)

    context = {
        'room_messages': room_messages,
        'participants': participants,
        'room': room,
    }
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def room_form(request):
    topics = Topic.objects.all()
    form = RoomForm()
    context = {
        'form': form,
        'topics': topics,
    }
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.link = room.name.replace(' ', '_').lower()
            room.save()
            form.save_m2m()
            return redirect('home')
        else:
            messages.error(
                request, 'An error has occurred during room creation')
            return render(request, 'base/room_form.html', context)
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    context = {
        'form': form,
        'topics': topics,
        'room': room,
    }
    if request.user != room.host:
        return HttpResponse('You are not authorized to view this page')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not authorized to view this page')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {
        'item': room
    }
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def delete_message(request, pk):
    room_message = Message.objects.get(id=pk)
    print(request.user)
    print(room_message.user)
    if request.user != room_message.user:
        return HttpResponse('You are not authorized to view this page')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {
        'item': room_message
    }
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def update_user(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.user != user:
        return HttpResponse('You are not authorized to view this page')
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=pk)
        else:
            return HttpResponse('Form is not valid')
    return render(request, 'base/edit_user.html', {'form': form})
