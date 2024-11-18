"""
URL configuration for task_user_meneger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os.path import basename

from django.contrib import admin
from django.urls import path, include

from tasks.views import TaskViewSet
from users.views import UserViewSet
from rest_framework import routers

router1 = routers.SimpleRouter()
router1.register(r'tasks', TaskViewSet, basename='tasks')

router2 = routers.SimpleRouter()
router2.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router1.urls)),  # http://127.0.0.1:8000/api/v1/tasks/
    path('api/v2/', include(router2.urls)),  # http://127.0.0.1:8000/api/v2/users/
]
