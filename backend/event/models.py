from django.db import models

from user_system.models import User


class Event(models.Model):
    user = models.ForeignKey(User, related_name="event", on_delete=models.CASCADE, null=True)
    nickname = models.CharField(max_length=45, null=True, blank=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    event_date = models.CharField(max_length=25, blank=True, null=True)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event', blank=True, null=True)
