
from django.test import TestCase

from roiback.models import Hotel, Room, Rate, Inventory


class IntegrationHotelTestCase(TestCase):

    def test_hotel_list(self):
        hotels = Hotel.objects.get_hotels()

        self.assertEqual(hotels.count(), 3)

    def test_hotel_detail(self):
        hotel = Hotel.objects.get_hotel_by_code('hc')

        self.assertEqual(hotel.name, 'Hotel Continental')


class IntegrationRoomTestCase(TestCase):

    def test_room_list(self):
        rooms = Room.objects.get_rooms()

        self.assertEqual(rooms.count(), 6)

    def test_room_by_hotel_id(self):
        hotel_mediterraneo_id = 2
        rooms = Room.objects.get_rooms_by_hotel_id(hotel_mediterraneo_id)

        self.assertEqual(rooms.count(), 2)
        self.assertEqual(rooms[0].name, 'Master Room')


class IntegrationRateTestCase(TestCase):

    def test_rate_list(self):
        rates = Rate.objects.get_rates()

        self.assertEqual(rates.count(), 6)

    def test_rate_by_room_codes(self):
        room_codes = ['hm-mr', 'hm-sr', 'hr-mr', 'hr-sr']
        rates = Rate.objects.get_rates_by_room_codes(room_codes)

        self.assertEqual(rates.count(), 4)
        self.assertEqual(rates[0].name, 'Rate 1')


class IntegrationInventoryTestCase(TestCase):

    def test_inventory_by_rate_codes_and_dates(self):
        rate_codes = ['hm-mr-rt-1', 'hm-sr-rt-2']
        checkin_date = '2021-03-15'
        checkout_date = '2021-03-16'
        inventories = Inventory.objects.get_inventories_from_rate_codes_and_dates(rate_codes, checkin_date, checkout_date)

        self.assertEqual(inventories.count(), 4)
        self.assertEqual(inventories[0].get('price'), 200)