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
        read_only_fields = ['task_user']

        def update(self, instance, validated_data):
            """
            Обновление задачи. Убираем поле 'task_user' из validated_data,
            чтобы предотвратить изменение пользователя задачи.
            """
            validated_data.pop('task_user', None)
            return super().update(instance, validated_data)


