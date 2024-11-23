from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

