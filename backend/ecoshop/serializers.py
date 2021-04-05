from rest_framework import serializers

from ecoshop.models import ShopPost, ShopPostImage


class ShopPostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ShopPostImage
        fields = ['image']


class ShopSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.shopimage_set.all()
        return ShopPostImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = ShopPost
        fields = ('id', 'name', 'address', 'content', 'heart_cnt', 'heart', 'report', 'images')

    def create(self, validated_data):
        instance = ShopPost.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            ShopPostImage.objects.create(shop=instance, image=image_data)
        return instance
