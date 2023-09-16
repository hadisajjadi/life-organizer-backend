from rest_framework import serializers
from .models import Task
from accounts.serializers import AccountSerializer  # Make sure to import the appropriate AccountSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'due_date', 'start_time', 'finish_time', 'user')
        read_only_fields = ['user']