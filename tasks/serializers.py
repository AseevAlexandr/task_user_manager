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

        def update(self, instance, validated_data):
            # Удаляем 'task_user' из данных для обновления
            validated_data.pop('task_user', None)

            return super().update(instance, validated_data)


