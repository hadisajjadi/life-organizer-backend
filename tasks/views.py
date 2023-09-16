from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer  # Replace with the appropriate serializer for Task

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer  # Replace with the appropriate serializer for Task
    permission_classes = [permissions.IsAuthenticated]
    read_only_fields = ['user']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)