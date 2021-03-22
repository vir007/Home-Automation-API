from rest_framework.permissions import BasePermission, SAFE_METHODS

# Custom Permission Class:
#   -> Everyone can Retrive the data
#   -> Only admin can Create, Update or destroy the data 
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff