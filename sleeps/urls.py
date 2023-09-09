from django.urls import path, include
from rest_framework import routers
from .views import SleepViewSet

router = routers.DefaultRouter()
router.register(r'sleep', SleepViewSet, basename='sleep')

urlpatterns = [
    path('', include(router.urls)),
]