from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ecoshop.models import Shop
from ecoshop.serializers import ShopSerializer


class EcoShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Shop.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
