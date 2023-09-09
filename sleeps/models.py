import uuid
from django.db import models
from accounts.models import Account

class Sleep(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    duration = models.FloatField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.email} - {self.date} - {self.duration}"