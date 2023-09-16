from rest_framework import serializers
from .models import Sleep
from accounts.serializers import AccountSerializer

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ('id', 'date', 'duration', 'user')
        read_only_fields = ['user']