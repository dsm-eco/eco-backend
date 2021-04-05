from django.db import models

from user_system.models import User


class ShopPost(models.Model):
    user = models.ForeignKey(User, related_name="shop_post", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    content = models.CharField(max_length=200, blank=True, null=True)
    heart_cnt = models.IntegerField(default=0, blank=True, null=False)
    heart = models.BooleanField(default=False, blank=True)
    report = models.IntegerField(default=0, blank=True, null=False)


class ShopPostImage(models.Model):
    shop = models.ForeignKey(ShopPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop-post', blank=True, null=True)
