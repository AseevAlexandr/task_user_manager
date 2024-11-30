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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from tasks.views import TaskViewSet
from users.views import UserViewSet
from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your API Title",
      default_version='v1',
      description="Описание вашего API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourcompany.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router1 = routers.SimpleRouter()
router1.register(r'tasks', TaskViewSet, basename='tasks')

router2 = routers.SimpleRouter()
router2.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(router1.urls)),  # http://127.0.0.1:8000/api/v1/tasks/
    path('api/v2/', include(router2.urls)),  # http://127.0.0.1:8000/api/v2/users/

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # http://127.0.0.1:8000/api/token/
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # http://127.0.0.1:8000/api/token/refresh/
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # http://127.0.0.1:8000/api/token/verify/

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# User_1
# fghj1234
