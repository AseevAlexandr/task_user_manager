from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializers

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return super().get_permissions()


def index_page(request):
    return render(request, 'index.html')
