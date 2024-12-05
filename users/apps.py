from django.apps import AppConfig

"""Этот файл содержит настройки и конфигурацию для приложения 'users'. 
Django использует этот файл для регистрации приложения в проекте и применения
соответствующих настроек, таких как тип автоинкрементируемых полей."""

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
