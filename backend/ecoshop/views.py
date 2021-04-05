from rest_framework import viewsets

from ecoshop.models import Shop
from ecoshop.serializers import ShopSerializer


class EcoShopViewSet(viewsets.GenericViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
