from django.contrib.admin.utils import model_ngettext
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
"""
Создаём модель User из встроенной в Django модели
"""
