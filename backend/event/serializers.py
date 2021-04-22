from rest_framework import serializers

from event.models import EventImage, Event


class EventImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = EventImage
        fields = ['image']


class EventSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    heart_cnt = serializers.SerializerMethodField()
    heart = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.eventimage_set.all()
        return EventImageSerializer(instance=image, many=True, context=self.context).data

    def get_heart_cnt(self, obj):
        return obj.count_likes_user()

    def get_heart(self, obj):
        user = self.context.get('request').user
        if obj.event_likes_user.filter(id=user.id).exists():
            return True
        else:
            return False

    class Meta:
        model = Event
        fields = ('id', 'content', 'heart_cnt', 'heart', 'event_date', 'images')

    def create(self, validated_data):
        instance = Event.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            EventImage.objects.create(event=instance, image=image_data)
        return instance
