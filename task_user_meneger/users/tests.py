from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserViewSetTest(APITestCase):

    def setUp(self):
        """
        Этот метод выполняется перед каждым тестом.
        Мы создаем тестового пользователя, чтобы использовать его в тестах.
        """
        self.test_user = User.objects.create_user(username='testuser', email='testuser@example.com',
                                                  password='password123')
        self.test_user.is_active = True
        self.test_user.save()

        self.url = reverse('api/v2/users/')  # Получаем URL для списка пользователей (UserViewSet)

    def test_create_user(self):
        """
        Проверяем, что можно создать нового пользователя.
        """
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
