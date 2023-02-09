from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('profile/edit/<str:pk>/', views.update_user, name='edit-profile'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('room_form/', views.room_form, name='room-form'),
    path('update_room/<str:pk>/', views.update_room, name='update-room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete-room'),
    path('delete_message/<str:pk>/', views.delete_message, name='delete-message'),
    path('topics/', views.topics, name='topics'),
    path('recent/', views.activity, name='recent-activity'),
]