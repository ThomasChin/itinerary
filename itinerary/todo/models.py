from django.db import models

from itinerary.models import TimeStampedModel
from itinerary.users.models import User


class Todo(TimeStampedModel):
    description = models.CharField(max_length=64)
    notes = models.TextField(max_length=1024, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(blank=True, null=True)