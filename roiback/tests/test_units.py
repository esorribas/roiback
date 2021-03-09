from django.test import TestCase

from roiback.api.services.hotel_service import HotelService


class SerializerHotelServiceTestCase(TestCase):

    def setUp(self):
        self.service = HotelService()

    def test_get_rates_data(self):
        test_rate_list = [ 'rt1', 'rt2', 'rt3', 'rt4', 'rt5', 'rt6', 'rt7', 'rt8', 'rt9', 'rt10' ]
        test_room_dict = { 'rm-1': [ 'rt1', 'rt2', 'rt3' ], 'rm-2': [ 'rt4', 'rt5', 'rt6', 'rt7' ], 'rm-3': [ 'rt8', 'rt9', 'rt10' ] }
        data = [
            { 'code': 'rt1', 'room__code': 'rm-1', 'room_id': 1 },
            { 'code': 'rt2', 'room__code': 'rm-1', 'room_id': 1 },
            { 'code': 'rt3', 'room__code': 'rm-1', 'room_id': 1 },
            { 'code': 'rt4', 'room__code': 'rm-2', 'room_id': 1 },
            { 'code': 'rt5', 'room__code': 'rm-2', 'room_id': 1 },
            { 'code': 'rt6', 'room__code': 'rm-2', 'room_id': 1 },
            { 'code': 'rt7', 'room__code': 'rm-2', 'room_id': 1 },
            { 'code': 'rt8', 'room__code': 'rm-3', 'room_id': 1 },
            { 'code': 'rt9', 'room__code': 'rm-3', 'room_id': 1 },
            { 'code': 'rt10', 'room__code': 'rm-3', 'room_id': 1 },
        ]

        rates_codes, rooms_dict = self.service.get_rates_data(data)

        self.assertEqual(rates_codes, test_rate_list)
        self.assertEqual(rooms_dict, test_room_dict)

