from django.forms import ModelForm

from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants', 'link']  

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        # exclude = ['is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'groups', 'user_permissions']