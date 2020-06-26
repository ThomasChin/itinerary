from django.db import models

from mcc.models import TimeStampedModel
from mcc.users.models import User


class Todo(TimeStampedModel):
    description = models.CharField(max_length=64)
    notes = models.TextField(max_length=1024, default="", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
