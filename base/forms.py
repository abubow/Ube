from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants', 'link']  

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'avatar', 'email', 'bio'] 

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
