import datetime

from django.test import TestCase

from roiback.api.serializer.hotel_serializer import HotelSerializer
from roiback.api.serializer.room_serializer import RoomSerializer
from roiback.api.serializer.rate_serializer import RateSerializer
from roiback.api.serializer.inventory_serializer import InventorySerializer

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

        assert results == expected_results


class SerializerRoomTestCase(TestCase):

    def test_expected_serialized_json(self):
        expected_results = {
            'id': 1,
            'name': 'Master Room',
            'code': 'hc-mr',
            'hotel_id': 1,
            'created_date': str(datetime.datetime.now())
        }

        room = Room(**expected_results)

        results = RoomSerializer(room).data

        assert results == expected_results


class SerializerRateTestCase(TestCase):

    def test_expected_serialized_json(self):
        expected_results = {
            'id': 1,
            'name': 'Rate 1',
            'code': 'hc-mr-rt-1',
            'room_id': 1,
            'created_date': str(datetime.datetime.now())
        }

        rate = Rate(**expected_results)

        results = RateSerializer(rate).data

        assert results == expected_results


class SerializerInventoryTestCase(TestCase):

    def test_expected_serialized_json(self):
        expected_results = {
            'id': 1,
            'price': 150,
            'rate_id': 1,
            'created_date': str(datetime.datetime.now())
        }

        inventory = Inventory(**expected_results)

        results = InventorySerializer(inventory).data

        assert results == expected_results