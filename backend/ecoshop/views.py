import json

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ecoshop.models import ShopPost, Shop
from ecoshop.serializers import ShopPostSerializer, ShopSerializer


class ShopPostViewSet(viewsets.ModelViewSet):
    serializer_class = ShopPostSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = ShopPost.objects.select_related('user').filter(permission=False)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, nickname=self.request.user.nickname)

    def get_serializer_context(self):
        context = super(ShopPostViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

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

        if instance.shop_post_likes_user.filter(id=user.id).exists():
            instance.shop_post_likes_user.remove(user)
            message = 'false'
        else:
            instance.shop_post_likes_user.add(user)
            message = 'true'

        context = {'heart_cnt': instance.count_likes_user(), 'heart': message}
        return HttpResponse(json.dumps(context), content_type="application/json")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ecoshop_list(request):
    data = request.data["location"]

    addr1 = address_finder(data['1'], data['2'])
    addr2 = address_finder(data['3'], data['4'])
    address = address_finder(addr1, addr2)

    queryset = Shop.objects.filter(address__startswith=address)
    serializer = ShopSerializer(queryset, many=True)

    return Response(serializer.data)


def address_finder(addr1, addr2):
    result = ""
    len1, len2 = len(addr1), len(addr2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if i + j < len1 and addr1[i + j] == addr2[j]:
                match += addr2[j]
            else:
                if len(match) > len(result):
                    result = match
                match = ""
    return result
