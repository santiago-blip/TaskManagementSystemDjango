from rest_framework import permissions

class HasJoinPermission(permissions.BasePermission):

                                                                                                
    def has_object_permission(self, request, view, obj):
        objModel,taskModel = obj
        if not bool(request.user and request.user.is_authenticated):
            return False
        
        if not request.user.is_verified:
            return False
        
        
        return objModel.user == request.user and taskModel.user == request.user
