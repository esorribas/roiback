
from django.http import Http404
from django.forms.models import model_to_dict

from roiback.models import Hotel, Room, Rate, Inventory


class HotelService:

    def get_all_hotels(self):
        '''
            This method returns all hotels
            Returns a list of hotels (code and name)
        '''

        return list(Hotel.objects.values('code', 'name').order_by('-created_date'))

    def get_hotel_details(self, hotel_code):
        '''
            This method returns the hotel details
            Returns the hotel object
        '''

        try:
            hotel = Hotel.objects.get(code=hotel_code)

            return model_to_dict(hotel)
        except Hotel.DoesNotExist:
            raise Http404()

    def get_result_rates(self, inventories, rates_list):
        '''
            This method helps to obtain the final data with rates and inventory prices.
            Returns a list with the rates (key) and calculated data (dictionary with prices and dates)
        '''

        rates = []

        if rates_list:
            inventories_dict = self.get_inventories_from_rates(inventories, rates_list)
                        
            for rate_code in rates_list:
                inventories_list = inventories_dict.get(rate_code, [])
                
                if inventories_list:
                    # Sum total values outside query to improve performance (avoids make query twice)
                    total_price = sum([il.get('price') for il in inventories_list])

                    rates.append({
                        rate_code: {
                            'total_price': total_price,
                            'breakdown': inventories_list
                        }
                    })

        return rates

    def get_inventories_from_rates(self, inventories, rates):
        '''
            This method helps to obtain a structured data related between inventories and rates.
            Returns a dictionary with the rates (key) and inventories (list of inventory objects)
        '''

        inventories_dict = {}

        for inventory in inventories:
            rate_code = inventory.get('rate__code')
            price = inventory.get('price')
            date = inventory.get('date')

            if rate_code in rates:
                inventory_data = { 'date': date.strftime('%Y-%m-%d'), 'price': price }

                if rate_code in inventories_dict:
                    inventories_dict[rate_code].append(inventory_data)
                else:
                    inventories_dict[rate_code] = [ inventory_data ]

        return inventories_dict


    def get_rates_data(self, rates):
        '''
            This method helps to obtain a structured data related with rates and rooms.
            Returns a tuple with:
                - List with rate codes 
                - Dictionary with the rooms (key) and rates (list of rate codes)
        '''

        rooms_dict = {}
        rates_codes = []

        for rate in rates:
            room_code = rate.get('room__code')
            rate_code = rate.get('code')

            rates_codes.append(rate_code)

            if room_code in rooms_dict.keys():
                rooms_dict[room_code].append(rate_code)
            else:
                rooms_dict[room_code] = [ rate_code ]

        return rates_codes, rooms_dict


    def get_available_rooms_by_dates(self, hotel_code, checkin_date, checkout_date):
        '''
            This method returns all rooms available by hotel, checkin and checkout dates
            Returns a list of rooms with related rates and inventories 
        '''

        rooms = []

        # First of all, ensure hotel exists, if not raise a HTTP 404 error.
        hotel = self.get_hotel_details(hotel_code)

        # Get all room codes according hotel
        room_codes = Room.objects.filter(hotel_id=hotel.get('id')).values_list('code', flat=True)

        # Get all rates from hotel rooms
        rates = Rate.objects.select_related('room').filter(room__code__in=room_codes).values('code', 'room__code', 'room__id')

        # Get all rate codes, and a structured dictionary with the relationship room:rates
        rates_codes, rooms_dict = self.get_rates_data(rates)

        # Get all inventories related with rates ids, checkin and checkout dates
        inventories = Inventory.objects.select_related('rate')\
            .filter(rate__code__in=rates_codes, date__gte=checkin_date, date__lte=checkout_date)\
            .values('rate__code', 'date', 'price')

        # Iterate evert room and ensure if exists rates for the room
        # if not exists, skip room to avoid empty results
        for room_code in room_codes:
            if room_code in rooms_dict:
                rates_list = rooms_dict.get(room_code, [])
                rates = self.get_result_rates(inventories, rates_list)

                if rates:
                    rooms.append({
                        room_code: {
                            'rates': rates
                        }
                    })

        return rooms
