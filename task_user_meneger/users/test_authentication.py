# users/tests/test_authentication.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        """Создаем тестового пользователя для аутентификации"""
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
        self.user = User.objects.create_user(**self.user_data)

    def _get_token_for_user(self, user):
        """Получаем токен для аутентификации пользователя"""
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_login(self):
        """Тест аутентификации пользователя"""
        data = {
            "username": "testuser",
            "password": "password123"
        }
        response = self.client.post('/api/token/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_unauthorized_access(self):
        """Тест для доступа без токена"""
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
