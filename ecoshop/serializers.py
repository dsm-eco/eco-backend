import django.db.models.fields
from rest_framework import serializers

from ecoshop.models import ShopImage, Shop


class ShopImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ShopImage
        fields = ['image']


class ShopSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.shopimage_set.all()
        return ShopImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'content', 'images')
