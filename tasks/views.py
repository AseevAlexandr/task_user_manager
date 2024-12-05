from django.template.context_processors import request
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import Tasks
from .serializers import TasksSerializers

class IsAuthorOnly(BasePermission):
    """
    Класс определяющий разрешения на создание, изменения, удаление задачи только для автора
    """
    def has_object_permission(self, request, view, obj):
        """ функция проверяет, является ли текущий пользователь автором задачи, и если да, то разрешает ему доступ"""
        if request.user == obj.author:
            return True


class TaskViewSet(viewsets.ModelViewSet):
    """
    Класс возвращающий авторизованному пользователю данные о его задачах
    """
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
    permission_classes = [IsAuthenticated, IsAuthorOnly]

    def perform_update(self, serializer):
        serializer.validated_data.pop('task_user', None)
        serializer.save()

    def get_queryset(self):
        """
        Возвращает задачи, связанные с текущим пользователем (пользователь должен быть авторизован).
        """
        return Tasks.objects.filter(task_user=self.request.user)
