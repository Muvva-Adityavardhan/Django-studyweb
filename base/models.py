from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
                            
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True) #auto_now --> Time stamp at every time we add 
    created = models.DateTimeField(auto_now_add=True) #auto_now_add --> Time stamp at the time of creation only
    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE) # SET_NULL --> If parent is deleted, then it will be set as Null, Cascade --> Delete
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #auto_now --> Time stamp at every time we add 
    created = models.DateTimeField(auto_now_add=True) #auto_now_add --> Time stamp at the time of creation only

    def __str__(self):
        return self.body[0:50]