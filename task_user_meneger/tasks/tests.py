# tasks/tests/test_tasks.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Tasks
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class TaskTests(APITestCase):
    def setUp(self):
        """Создаем тестового пользователя и задачу для использования в тестах"""
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = self._get_token_for_user(self.user)
        self.task_data = {
            "title": "Test Task",
            "description": "Test Task Description",
            "created_by": self.user.id
        }
        self.task = Tasks.objects.create(**self.task_data)

    def _get_token_for_user(self, user):
        """Получаем токен для аутентификации пользователя"""
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_create_task(self):
        """Тест создания новой задачи"""
        data = {
            "title": "New Task",
            "description": "New Task Description",
            "created_by": self.user.id
        }
        response = self.client.post('/api/v1/tasks/', data, format='json',
                                    HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Task')

    def test_get_task(self):
        """Тест получения задачи"""
        response = self.client.get(f'/api/v1/tasks/{self.task.id}/',
                                   HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        """Тест обновления задачи"""
        data = {
            "title": "Updated Task",
            "description": "Updated Task Description"
        }
        response = self.client.put(f'/api/v1/tasks/{self.task.id}/', data, format='json',
                                   HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        """Тест удаления задачи"""
        response = self.client.delete(f'/api/v1/tasks/{self.task.id}/',
                                      HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Проверяем, что задача действительно удалена
        task_exists = Tasks.objects.filter(id=self.task.id).exists()
        self.assertFalse(task_exists)
