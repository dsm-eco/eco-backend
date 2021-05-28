from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ecoshop_post.models import ShopPost
from ecoshop_post.serializers import ShopPostSerializer
from event.models import Event
from event.serializers import EventSerializer


class MyShopPostListViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ShopPostSerializer

    def get_queryset(self):
        queryset = ShopPost.objects.filter(user_id=self.request.user.id)
        return queryset

    def get_serializer_context(self):
        context = super(MyShopPostListViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class MyEventPostListViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.filter(user_id=self.request.user.id)
        return queryset

    def get_serializer_context(self):
        context = super(MyEventPostListViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
