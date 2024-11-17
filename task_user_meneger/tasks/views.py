from rest_framework import viewsets

from .models import Tasks
from .serializers import TasksSerializers


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
