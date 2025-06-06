from django.db import models

# Create your models here.

class Room(models.Model):
    #host =
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True) #auto_now --> Time stamp at every time we add 
    created = models.DateTimeField(auto_now_add=True) #auto_now_add --> Time stamp at the time of creation only
    def __str__(self):
        return self.name