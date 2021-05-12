from django.db import models

from user_system.models import User


class Shop(models.Model):
    name = models.CharField(max_length=45, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    content = models.CharField(max_length=200, blank=True, null=True)


class ShopImage(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop', blank=True, null=True)
