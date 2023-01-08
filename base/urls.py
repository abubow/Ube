from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('room_form/', views.room_form, name='room-form'),
    path('update_room/<str:pk>/', views.update_room, name='update-room'),
]