"""

This file contains the classes for the player layout. 

Each player is given an auto generated id from the UUID library
    The ID is also each players primary key
Each player can give themselves a name that is less than or equal to fifty characters

"""

from django.db import models
from uuid import uuid4

class Player(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    name = models.CharField(max_length=50,blank=False)
    #current room
