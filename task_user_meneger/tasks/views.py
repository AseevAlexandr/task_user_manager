from django.template.context_processors import request
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import Tasks
from .serializers import TasksSerializers

class IsAuthorOnly(BasePermission):
    def task_permission(self, request, view, obj):
        if request.user == obj.author:
            return True


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
    permission_classes = [IsAuthenticated, IsAuthorOnly]
