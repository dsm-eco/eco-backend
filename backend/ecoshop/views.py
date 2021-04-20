import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ecoshop.models import ShopPost
from ecoshop.serializers import ShopSerializer


class ShopPostViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = ShopPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, nickname=self.request.user.nickname)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user.id == self.request.user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def report(self, request, pk):
        instance = self.get_object()
        instance.report += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def heart(self, requset, pk):
        instance = self.get_object()
        user = requset.user

        if instance.likes_user.filter(id=user.id).exists():
            instance.likes_user.remove(user)
            message = '하트 취소'
        else:
            instance.likes_user.add(user)
            message = '하트 누르기'

        context = {'heart_cnt': instance.count_likes_user(), 'message': message}
        return HttpResponse(json.dumps(context), content_type="application/json")

