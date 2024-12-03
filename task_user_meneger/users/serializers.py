from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializers(serializers.ModelSerializer):
    """
    Класс обрабатывающий модель User и возвращающий заданные поля:
     'id', 'username', 'email', 'password'.
    Имеет обязательные поля для заполнения extra_kwargs.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'required': True}
        }

    def create(self, validated_data):
        """
        Функция create создаёт пользователя и делает его аккаунт активным для последующего использования.
        """
        user = User.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        return user
