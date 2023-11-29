from django.db import models
from apps.user.models import User


class myTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(disabled=False)

class BaseModel(models.Model):

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_ref',related_query_name='%(class)s_ref_query')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)

    class Meta:
        abstract = True