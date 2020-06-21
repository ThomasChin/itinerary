from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model for self-updating created/updated fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
