from rest_framework.viewsets import ModelViewSet

from roiback.models import Hotel
from roiback.api.serializer.hotel_serializer import HotelSerializer


class HotelViewSet(ModelViewSet):
    serializer_class = HotelSerializer

    def get_queryset(self):
        return Hotel.objects.get_hotels()