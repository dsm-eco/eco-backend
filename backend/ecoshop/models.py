from django.db import models

from user_system.models import User


class Shop(models.Model):
    user = models.ForeignKey(User, related_name="shop", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    heart_cnt = models.IntegerField(null=False, default=0)
    heart = models.BooleanField(default=False)
