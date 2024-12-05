from django.contrib import admin
from .models import Tasks
"""Регистрация приложения Tasks в панели администратора"""
admin.site.register(Tasks)
