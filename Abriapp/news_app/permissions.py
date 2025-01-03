from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'SUPER_USER'

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'ADMIN'
