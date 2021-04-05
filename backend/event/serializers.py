from rest_framework import serializers

from ecoshop.models import Shop, ShopImage
from event.models import EventImage, Event


class EventImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)

    class Meta:
        model = EventImage
        fields = ['image']


class EventSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):

        image = obj.diaryimage_set.all()
        return EventImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Event
        fields = ('id', 'content', 'heart_cnt', 'heart')

    def create(self, validated_data):
        instance = Shop.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            ShopImage.objects.create(event=instance, image=image_data)
        return instance
