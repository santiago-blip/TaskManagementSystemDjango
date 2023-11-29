from .BaseModel import BaseModel, myTaskManager
from .TaskModel import TaskModel
from django.db import models

class CategoryModel(BaseModel):
    title = models.CharField(max_length=15,unique=True)
    task = models.ManyToManyField(TaskModel)
    objects = models.Manager()
    myManager = myTaskManager()