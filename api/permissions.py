from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission): 
    """ 
    Класс для ограничения доступа к подпискам.
    Доступ только автору. 
    """ 

    message = 'Изменять подписку может только автор' 
 
    def has_object_permission(self, request, view, obj): 
        """ 
        Проверяет, что запрос сделан автором. 
        """ 

        return obj.author == request.user