from django.apps import AppConfig

"""Этот файл содержит класс конфигурации приложения, который наследуется от
AppConfig. Он отвечает за регистрацию приложения в проекте и определяет
основные настройки для работы приложения."""

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
