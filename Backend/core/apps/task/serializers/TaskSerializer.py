from rest_framework import serializers
from apps.task.models import TaskModel
from .StatusSerializer import StatusSerializer
from .CategorySerializer import CategorySerializer


class TaskSerializer(serializers.ModelSerializer):
    status = StatusSerializer(fields=('title',))
    categories = CategorySerializer(fields=('title',),source='categorymodel_set',many=True)
    class Meta:
        model = TaskModel
        fields = '__all__'