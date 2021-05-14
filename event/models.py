from django.conf import settings
from django.db import models

from user_system.models import User


class Event(models.Model):
    user = models.ForeignKey(User, related_name="event", on_delete=models.CASCADE, null=True)
    nickname = models.CharField(max_length=45, null=True, blank=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    event_date = models.CharField(max_length=25, blank=True, null=True)

    event_likes_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='event_likes_user',
        through='EventLike',
    )

    def count_likes_user(self):
        return self.event_likes_user.count()


class EventLike(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event', blank=True, null=True)
