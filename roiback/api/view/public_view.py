
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status

from roiback.api.services.hotel_service import HotelService
from roiback.api.serializer.hotel_serializer import HotelSerializer
from roiback.constants import ONE_MINUTE_SECONDS


class PublicHotelListView(ReadOnlyModelViewSet):
    serializer_class = HotelSerializer

    @method_decorator(cache_page(ONE_MINUTE_SECONDS))
    def list(self, request):
        service = HotelService()
        hotels = service.get_all_hotels()
        
        return Response(hotels, status=status.HTTP_200_OK)


class PublicHotelDetailView(ReadOnlyModelViewSet):
    serializer_class = HotelSerializer

    @method_decorator(cache_page(ONE_MINUTE_SECONDS))
    def retrieve(self, request, hotel_code):
        service = HotelService()
        hotel = service.get_hotel_details(hotel_code)

        return Response(hotel, status=status.HTTP_200_OK)


class PublicRoomAvailabilityListView(ReadOnlyModelViewSet):

    @method_decorator(cache_page(ONE_MINUTE_SECONDS))
    def list(self, request, hotel_code, checkin_date, checkout_date):
        service = HotelService()
        rooms = service.get_available_rooms_by_dates(hotel_code, checkin_date, checkout_date)
        
        if rooms:
            return Response({ 'rooms': rooms }, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
