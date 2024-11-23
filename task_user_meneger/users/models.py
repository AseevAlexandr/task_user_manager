from django.contrib.admin.utils import model_ngettext
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     is_active =  models.BooleanField('active', default=True,)
#
#     def __str__(self):
#         return self.name
