from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        return user
