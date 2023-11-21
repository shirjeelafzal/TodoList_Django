# myapp/permissions.py

from rest_framework import permissions

class MyPermission(permissions.BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # Check user-specific permissions (replace with your actual field names)
            can_read = getattr(request.user, 'view', False)
            can_write = getattr(request.user, 'edit', False)
            admin=getattr(request.user,'is_admin',False)
            # Allow read permission
            if admin:
                return True
            elif view.action in ['list', 'retrieve']:
                return can_read

            # Allow to write permission
            elif view.action in ['create', 'update', 'partial_update', 'destroy']:
                return can_write

        return False
