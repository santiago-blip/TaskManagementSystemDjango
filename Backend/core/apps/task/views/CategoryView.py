from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.task.models import CategoryModel
from apps.user.models import User
from apps.task.serializers.CategorySerializer import CategorySerializer
from apps.task.permissions.TaskPermission import HasTaskPermission

from django.http import Http404

class CategoryView(APIView):
    permission_classes = [HasTaskPermission]

    def get_object(self,id):
        pk = id
        obj = None
        if pk:
            obj = CategoryModel.myManager.filter(pk=pk).first()
            if not obj:
                raise Http404
            self.check_object_permissions(self.request, obj)
            return obj
        self.check_object_permissions(self.request, obj)
        return CategoryModel.myManager.filter(user__id=self.request.user.id)
    
    def get(self,request,pk = None,*args,**kwargs):
        query = self.get_object(pk)
        if pk:
            data = CategorySerializer(query)
        else:
            data = CategorySerializer(query,many=True)
        return Response({'response':data.data},status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        self.check_object_permissions(request,None)
        data = CategorySerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save(user=request.user)
        return Response({'response':'Category has been created.'},status=status.HTTP_201_CREATED)

    def put(self,request,pk = None,*args,**kwargs):
        if not pk:
            return Response({'error':'No id given.'},status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object(pk)
        data = CategorySerializer(instance,data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Category  updated.'},status=status.HTTP_200_OK)

    def delete(self,request,pk = None,*args,**kwargs):
        if not pk:
            return Response({'error':'No id given.'},status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object(pk)
        instance.disabled = True
        instance.save()
        return Response({'response':'Category  deleted.'},status=status.HTTP_200_OK)