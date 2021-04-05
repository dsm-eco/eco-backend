from rest_framework import serializers

from ecoshop.models import Shop, ShopImage


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
        fields = ('id', 'name', 'address', 'content', 'heart_cnt', 'heart', 'report', 'images')

    def create(self, validated_data):
        instance = Shop.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            ShopImage.objects.create(shop=instance, image=image_data)
        return instance
