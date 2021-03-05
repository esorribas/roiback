from rest_framework.viewsets import ModelViewSet

from roiback.models import Room
from roiback.api.serializer.room_serializer import RoomSerializer


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.get_rooms()
