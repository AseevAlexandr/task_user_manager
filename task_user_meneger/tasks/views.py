from django.template.context_processors import request
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import Tasks
from .serializers import TasksSerializers

class IsAuthorOnly(BasePermission):
    """
    Класс определяющий разрешения на создание, изменения, удаление задачи только для автора
    """
    def task_permission(self, request, view, obj):
        if request.user == obj.author:
            return True


class TaskViewSet(viewsets.ModelViewSet):
    """
    Класс возвращающий авторизованному пользователю данные о его задачах
    """
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
    permission_classes = [IsAuthenticated, IsAuthorOnly]
