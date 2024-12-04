from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializers

class UserViewSet(ModelViewSet):
    """
    Класс управляет операциями CRUD (создание, чтение, обновление, удаление) для модели User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_permissions(self):
        """
        Функция определяет разрешение на создание пользователя(для всех),
        и упрвление аккаунтом(тоько для авторизованного пользователя )
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return super().get_permissions()


def index_page(request):
    """
    Функция обрабатывает html страницу и возвращает ее пользователю как стартовую
    """
    return render(request, 'index.html')