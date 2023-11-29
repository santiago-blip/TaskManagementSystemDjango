from rest_framework import permissions

class HasTaskPermission(permissions.BasePermission):

                                                                                                
    def has_object_permission(self, request, view, obj):
        
        if not bool(request.user and request.user.is_authenticated):
            return False
        
        if not request.user.is_verified:
            return False

        if request.method == 'POST':
            return True
        
        if not obj and request.user:
            return True
        # return obj == request.user or request.user.is_admin
        return obj.user == request.user
