from django.db import models
from django.utils.timezone import now
from django.db.models import URLField


class Companies(models.Model):
    class Companystatus(models.TextChoices):
        LAYOFF = ("Layoff",)
        HIRING_FREEZE = ("Hiring Freeze",)
        HIRING = "Hiring"

    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        choices=Companystatus.choices, default=Companystatus.HIRING, max_length=30
    )
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
