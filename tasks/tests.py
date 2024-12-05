from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Tasks


class TaskAPITests(APITestCase):

    def setUp(self):
        """Создадим пользователей для тестов"""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.other_user = User.objects.create_user(username="otheruser", password="otherpassword")
        """Логинимся для тестов"""
        self.client = APIClient()
        """Получаем JWT токен для аутентификации"""
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        """Создаем задачу для теста"""
        self.task_data = {
            'task_title': 'Test Task',
            'task_content': 'Content of test task',
            'task_status': 'новая',
            'task_user': self.user.id
        }

    def test_create_task(self):
        """Тест на создание задачи"""
        response = self.client.post('/api/v1/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['task_title'], self.task_data['task_title'])

    def test_create_task_unauthorized(self):
        """Тест на создание задачи без авторизации"""
        self.client.credentials()
        response = self.client.post('/api/v1/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_task(self):
        """Тест на получение задачи"""
        task = Tasks.objects.create(
            task_title='Test Task',
            task_content='Content of test task',
            task_status='новая',
            task_user=self.user
        )
        response = self.client.get(f'/api/v1/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['task_title'], task.task_title)
        self.assertEqual(response.data['task_user'], self.user.id)

    def test_update_task(self):
        """Тест на обновление задачи"""
        task = Tasks.objects.create(
            task_title='Test Task',
            task_content='Content of test task',
            task_status='новая',
            task_user=self.user
        )
        updated_data = {'task_title': 'Updated Test Task'}
        response = self.client.patch(f'/api/v1/tasks/{task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['task_title'], updated_data['task_title'])


    def test_delete_task(self):
        """Тест на удаление задачи"""
        task = Tasks.objects.create(
            task_title='Test Task',
            task_content='Content of test task',
            task_status='новая',
            task_user=self.user
        )
        response = self.client.delete(f'/api/v1/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Tasks.objects.filter(id=task.id).exists())

    def test_delete_task_unauthorized(self):
        """Тест на удаление задачи без авторизации"""
        """Создаем задачу и связываем с пользователем"""
        task = Tasks.objects.create(
            task_title='Test Task',
            task_content='Content of test task',
            task_status='новая',
            task_user=self.user
        )
        """Убираем авторизацию"""
        self.client.credentials()  # Очищаем токен
        """Пытаемся удалить задачу без авторизации"""
        response = self.client.delete(f'/api/v1/tasks/{task.id}/')
        """Проверяем, что ответ имеет статус 401 Unauthorized"""
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_task_validation(self):
        """Тест на валидацию задачи"""
        data = {
            'task_title': 'Test Task',
            'task_content': 'Content of test task',
            'task_status': 'новая',
            'task_user': self.user.id
        }
        response = self.client.post('/api/v1/tasks/', data, format='json')
        """Проверяем, что задача успешно создана"""
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['task_title'], 'Test Task')
        """Проверяем, что в ответе возвращается ID пользователя, а не сам объект"""
        self.assertEqual(response.data['task_user'], self.user.id)

    def test_task_status_choices(self):
        """Тест на валидацию статуса задачи"""
        valid_data = {
            'task_title': 'Valid task title',
            'task_content': 'Content for valid task',
            'task_status': 'в процессе',
            'task_user': self.user.id
        }
        response = self.client.post('/api/v1/tasks/', valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        invalid_data = valid_data.copy()
        invalid_data['task_status'] = 'неизвестный статус'
        response = self.client.post('/api/v1/tasks/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('task_status', response.data)
