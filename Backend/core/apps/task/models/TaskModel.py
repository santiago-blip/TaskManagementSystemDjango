from .BaseModel import BaseModel,myTaskManager
from .StatusModel import StatusModel
from django.db import models


    
class TaskModel(BaseModel):

    objects = models.Manager()
    myManager = myTaskManager()
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    status = models.ForeignKey(StatusModel,on_delete=models.SET_NULL,null=True)