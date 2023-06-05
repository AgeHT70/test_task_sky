from rest_framework import permissions


class IsActiveUserPermission(permissions.IsAuthenticated):
    message = 'Only active users has API permission'

    def has_permission(self, request, view):
        return request.user.is_active
