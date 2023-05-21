from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=250, null=True, unique=True)
    bio = models.TextField(null=True, blank=True)

    avatar = models.ImageField(
        null=True, blank=True, default='default.svg'
    )
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # pass

class Room(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=50, unique=True)
    # delete the room when the last topic it belongs to is deleted
    topics = models.ManyToManyField('Topic', related_name='rooms', blank=True)
    participants = models.ManyToManyField(
        User, related_name='rooms_joined', blank=True)
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='rooms_hosted')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-created']


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.message
