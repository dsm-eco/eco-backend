from rest_framework import serializers

from ecoshop.models import Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'content', 'heart_cnt', 'heart')
