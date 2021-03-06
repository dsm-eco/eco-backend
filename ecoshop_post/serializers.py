from rest_framework import serializers

from ecoshop_post.models import ShopPostImage, ShopPost


class ShopPostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ShopPostImage
        fields = ['image']


class ShopPostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    heart_cnt = serializers.SerializerMethodField()
    heart = serializers.SerializerMethodField()

    user_id = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    def get_images(self, obj):
        image = obj.shoppostimage_set.all()
        return ShopPostImageSerializer(instance=image, many=True, context=self.context).data

    def get_heart_cnt(self, obj):
        return obj.count_likes_user()

    def get_heart(self, obj):
        user = self.context.get('request').user
        if obj.shop_post_likes_user.filter(id=user.id).exists():
            return True
        else:
            return False

    def create(self, validated_data):
        instance = ShopPost.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            ShopPostImage.objects.create(shop_post=instance, image=image_data)
        return instance

    class Meta:
        model = ShopPost
        fields = ('id', 'user_id', 'nickname', 'name', 'address', 'content', 'heart_cnt', 'heart', 'report', 'images')
