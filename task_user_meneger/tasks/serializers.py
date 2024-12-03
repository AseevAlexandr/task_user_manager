from rest_framework import serializers
from .models import Tasks


class TasksSerializers(serializers.ModelSerializer):
    """
    Сериализатор задачи.
    Принимает модель задачи, после обработки возвращает все поля заданные в модели
    """
    class Meta:
        model = Tasks
        fields = '__all__'


