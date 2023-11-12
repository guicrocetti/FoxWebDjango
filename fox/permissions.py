from rest_framework import permissions

class CustomCreateUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verificar se o usuário é um administrador
        if request.user.is_superuser:
            return True

        # Verificar se o usuário é pessoal (staff)
        if request.user.is_staff:
            # Definir 'is_superuser' e 'is_staff' como False no request.data
            request.data['is_superuser'] = False
            request.data['is_staff'] = False
            return True

        return False
      
class ChangeSuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário tem permissão para modificar is_superuser
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Verifica se o usuário tem permissão para modificar is_superuser
        if request.user.is_superuser:
            return True
        return False