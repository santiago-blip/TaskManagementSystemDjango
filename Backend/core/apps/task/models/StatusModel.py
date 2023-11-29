from .BaseModel import BaseModel,myTaskManager
from django.db import models



    
class StatusModel(BaseModel):
    title = models.CharField(max_length=15,unique=True)
    objects = models.Manager()
    myManager = myTaskManager()

