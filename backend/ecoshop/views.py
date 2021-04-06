from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ecoshop.models import ShopPost
from ecoshop.serializers import ShopSerializer


class EcoShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = ShopPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, nickname=self.request.user.nickname)

    @action(detail=True, methods=['get'])
    def heart(self, request):
        instance = self.get_object()
        instance.heart = not instance.heart

        if not instance.heart:
            instance.heart_cnt -= 1
        else:
            instance.heart_cnt += 1

        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def report(self, request):
        instance = self.get_object()
        instance.report += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
