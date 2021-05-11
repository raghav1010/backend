from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

from rest_framework.routers import DefaultRouter

from .views import *

# router = DefaultRouter()
# router.register(r'User', LoginAPIView, basename="User")

urlpatterns = [
path('user', LoginAPIView.as_view({
    'get': 'list',
    'post': 'create',
    'put':'update'
}))]