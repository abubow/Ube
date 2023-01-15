from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('room_form/', views.room_form, name='room-form'),
    path('update_room/<str:pk>/', views.update_room, name='update-room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete-room'),
]