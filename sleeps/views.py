from rest_framework import viewsets, permissions
from .models import Sleep
from .serializers import SleepSerializer
from utils.permissions import IsOwnerOrAdmin

class SleepViewSet(viewsets.ModelViewSet):
    serializer_class = SleepSerializer
    permission_classes = [permissions.IsAuthenticated]
    read_only_fields = ['user']

    def get_queryset(self):
        return Sleep.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)