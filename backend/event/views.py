from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from event.models import Event
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Event.objects.all()

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
