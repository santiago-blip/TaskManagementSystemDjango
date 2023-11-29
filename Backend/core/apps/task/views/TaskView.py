from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.task.models import TaskModel
from apps.user.models import User
from apps.task.serializers.TaskSerializer import TaskSerializer
from apps.task.permissions.TaskPermission import HasTaskPermission

from django.http import Http404

class TaskView(APIView):
    permission_classes = [HasTaskPermission]

    def get_object(self,id):
        pk = id
        obj = None
        if pk:
            obj = TaskModel.myManager.filter(pk=pk).first()
            if not obj:
                raise Http404
            self.check_object_permissions(self.request, obj)
            return obj
        self.check_object_permissions(self.request, obj)
        return TaskModel.myManager.filter(user__id=self.request.user.id)
    
    def get(self,request,pk = None,*args,**kwargs):
        query = self.get_object(pk)
        if pk:
            data = TaskSerializer(query)
        else:
            data = TaskSerializer(query,many=True)
        return Response({'response':data.data},status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        self.check_object_permissions(request,None)
        data = TaskSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save(user=request.user)
        return Response({'response':'Task has been created.'},status=status.HTTP_201_CREATED)

    def put(self,request,pk = None,*args,**kwargs):
        if not pk:
            return Response({'error':'No id given.'},status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object(pk)
        data = TaskSerializer(instance,data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Task updated.'},status=status.HTTP_200_OK)

    def delete(self,request,pk = None,*args,**kwargs):
        if not pk:
            return Response({'error':'No id given.'},status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object(pk)
        instance.disabled = True
        instance.save()
        return Response({'response':'Task deleted.'},status=status.HTTP_200_OK)