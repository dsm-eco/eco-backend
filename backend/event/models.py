from django.db import models

from user_system.models import User


class Event(models.Model):
    user = models.ForeignKey(User, related_name="event", on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    heart_cnt = models.IntegerField(default=0, blank=True, null=False)
    heart = models.BooleanField(default=False, blank=True)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event', blank=True, null=True)
