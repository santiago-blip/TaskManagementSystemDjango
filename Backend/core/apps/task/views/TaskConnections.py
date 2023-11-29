from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.task.models import TaskModel,StatusModel, CategoryModel
from apps.user.models import User
from apps.task.serializers.TaskSerializer import TaskSerializer
from apps.task.permissions.JoinPermission import HasJoinPermission

from django.shortcuts import get_object_or_404


class TaskStatusView(APIView):
    permission_classes = [HasJoinPermission]

    def get_object(self,statusId,taskId):

        categoryQ = get_object_or_404(StatusModel,pk=statusId) 
        taskQ = get_object_or_404(TaskModel,pk=taskId) 

        self.check_object_permissions(self.request,obj=[categoryQ,taskQ])
        return categoryQ,taskQ

    def post(self,request,*args,**kwargs):
        statusId = request.data.get('status_id',None)
        taskId = request.data.get('task_id',None)
        if not statusId or not taskId:
            return Response({'error':'Make sure you are sending status_id and task_id'},status=status.HTTP_400_BAD_REQUEST)

        statusData,taskData = self.get_object(statusId,taskId)
        taskData.status = statusData
        taskData.save()
        # statusData.task.add(taskData)
        return Response(status=status.HTTP_200_OK)
    
    def delete(self,request,*args,**kwargs):
        statusId = request.data.get('status_id',None)
        taskId = request.data.get('task_id',None)
        if not statusId or not taskId:
            return Response({'error':'Make sure you are sending status_id and task_id'},status=status.HTTP_400_BAD_REQUEST)

        statusData,taskData = self.get_object(statusId,taskId)
        taskData.status = None
        taskData.save()
        return Response(status=status.HTTP_200_OK)
    
class TaskCategoryView(APIView):
    permission_classes = [HasJoinPermission]

    def get_object(self,categoryId,taskId):
        categoryQ = get_object_or_404(CategoryModel,pk=categoryId) 
        taskQ = get_object_or_404(TaskModel,pk=taskId) 

        self.check_object_permissions(self.request,obj=[categoryQ,taskQ])
        return categoryQ,taskQ

    def post(self,request,*args,**kwargs):
        categoryId = request.data.get('category_id',None)
        taskId = request.data.get('task_id',None)
        if not categoryId or not taskId:
            return Response({'error':'Make sure you are sending category_id and task_id'},status=status.HTTP_400_BAD_REQUEST)

        statusData,taskData = self.get_object(categoryId,taskId)
        statusData.task.add(taskData)
        return Response(status=status.HTTP_200_OK)
    
    def delete(self,request,*args,**kwargs):
        categoryId = request.data.get('category_id',None)
        taskId = request.data.get('task_id',None)
        if not categoryId or not taskId:
            return Response({'error':'Make sure you are sending category_id and task_id'},status=status.HTTP_400_BAD_REQUEST)

        statusData,taskData = self.get_object(categoryId,taskId)
        statusData.task.remove(taskData)
        return Response(status=status.HTTP_200_OK)