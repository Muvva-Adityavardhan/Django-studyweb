from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'), 

    path('create_room/', views.createRoom, name='create-room'),
    path('update_room/<str:pk>/', views.updateRoom, name='update-room'),
] 
# Even if you change the path, no need to change at every place as already name="" variable helps in how to access and use the url tag in the home.html file