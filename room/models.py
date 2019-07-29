"""

This file contains the classes for the room layout. 

"""

from django.db import models


# Create your models here.
class Room(models.Model):
    #Possible foreign key that connects each room
    #room number