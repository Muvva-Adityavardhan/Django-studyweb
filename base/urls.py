from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'), # str:pk means primary key, which is a unique identifier for each room
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('create_room/', views.createRoom, name='create-room'),
    path('update_room/<str:pk>/', views.updateRoom, name='update-room'),

    path('delete_room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete_message/<str:pk>/', views.deleteMessage, name='delete-message'),
    
    path('update_user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
] 
# Even if you change the path, no need to change at every place as already name="" variable helps in how to access and use the url tag in the home.html file