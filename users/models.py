from django.contrib.admin.utils import model_ngettext
from django.db import models
from django.contrib.auth import get_user_model

"""
Создаём переменную User, используя встроенную в Django модель get_user_model() кастомизируя её под задачи своего проекта
"""

User = get_user_model()

