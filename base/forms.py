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
        fields = ['name','avatar', 'username', 'email', 'bio']
        # exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'groups', 'user_permissions']

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        # exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'groups', 'user_permissions']