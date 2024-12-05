from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


class TokenMixin:
    def _get_token_for_user(self, user):
        """Получаем токен для аутентификации пользователя"""
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class AuthTests(APITestCase, TokenMixin):
    def setUp(self):
        """Создаем тестового пользователя для аутентификации"""
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
        self.user = User.objects.create_user(**self.user_data)

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


class UserTests(APITestCase, TokenMixin):
    def setUp(self):
        """Создаем тестового пользователя для использования в тестах"""
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = self._get_token_for_user(self.user)

    def test_create_user(self):
        """Тест создания нового пользователя"""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "password123"
        }
        response = self.client.post('/api/v2/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')

    def test_create_user_unauthorized(self):
        """Тест для создания пользователя без авторизации"""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "password123"
        }
        response = self.client.post('/api/v2/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        """Тест получения информации о пользователе"""
        response = self.client.get(f'/api/v2/users/{self.user.id}/',
                                   HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        """Тест обновления пользователя"""
        data = {
            "username": "updateduser",
            "email": "updateduser@example.com",
            "password": "newpassword123"
        }
        response = self.client.put(f'/api/v2/users/{self.user.id}/', data, format='json',
                                   HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'updateduser')

    def test_delete_user(self):
        """Тест удаления пользователя"""
        response = self.client.delete(f'/api/v2/users/{self.user.id}/',
                                      HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Проверяем, что пользователь действительно удален
        user_exists = User.objects.filter(id=self.user.id).exists()
        self.assertFalse(user_exists)

    def test_create_user_invalid(self):
        """Тест для создания пользователя с отсутствующим полем"""
        data = {
            "username": "newuser",
            "password": "password123"
            # email отсутствует
        }
        response = self.client.post('/api/v2/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


