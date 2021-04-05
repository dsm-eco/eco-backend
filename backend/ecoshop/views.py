from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ecoshop.models import ShopPost
from ecoshop.serializers import ShopSerializer


class EcoShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = ShopPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
