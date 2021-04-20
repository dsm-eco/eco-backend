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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user.id == self.request.user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
