from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet  # Replace SleepViewSet with TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')  # Change 'sleep' to 'task'

urlpatterns = [
    path('', include(router.urls)),
]