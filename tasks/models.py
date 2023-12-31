import uuid
from django.db import models
from django.utils import timezone
from accounts.models import Account
from projects.models import Project

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    finish_time = models.DateTimeField(null=True, blank=True)
    # todo - add repeatable field
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.name}"

    def save(self, *args, **kwargs):
        if self.due_date and (self.start_time or self.finish_time):
            raise ValueError("A task cannot have both a due date and start/finish times.")
        super().save(*args, **kwargs)