import datetime

from django.test import TestCase

from roiback.api.serializer.hotel_serializer import HotelSerializer
from roiback.models import Hotel, Room, Rate, Inventory


class SerializerHotelTestCase(TestCase):

    def test_expected_serialized_json(self):
        expected_results = {
            'id': 1,
            'name': 'Hotel Continental',
            'code': 'hc',
            'created_date': str(datetime.datetime.now())
        }

        hotel = Hotel(**expected_results)

        results = HotelSerializer(hotel).data

        print

        assert results == expected_results

