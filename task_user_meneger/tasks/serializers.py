from rest_framework import serializers
from .models import Tasks


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
