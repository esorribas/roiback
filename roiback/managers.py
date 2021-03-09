from django.db.models import Manager


class HotelManager(Manager):

    def get_hotels(self):
        queryset = self.get_queryset()

        return queryset.order_by('-created_date')

    def get_hotel_by_code(self, code):
        queryset = self.get_queryset()

        return queryset.get(code=code)


class RoomManager(Manager):

    def get_rooms(self):
        queryset = self.get_queryset()

        return queryset.order_by('-created_date')

    def get_rooms_by_hotel_id(self, hotel_id):
        queryset = self.get_queryset()

        return queryset.filter(hotel=hotel_id)
    
    def get_room_by_code(self, code):
        queryset = self.get_queryset()

        return queryset.get(code=code)


class RateManager(Manager):

    def get_rates(self):
        queryset = self.get_queryset()

        return queryset.order_by('-created_date')

    def get_rates_by_room_codes(self, room_codes):
        queryset = self.get_queryset()

        return queryset.select_related('room').filter(room__code__in=room_codes)

    def get_rate_by_code(self, code):
        queryset = self.get_queryset()

        return queryset.get(code=code)


class InventoryManager(Manager):

    def get_inventories(self):
        queryset = self.get_queryset()
        
        return queryset.order_by('-created_date')

    def get_inventories_from_rate_codes_and_dates(self, rate_codes, checkin_date, checkout_date):
        queryset = self.get_queryset()

        return queryset.select_related('rate')\
            .filter(rate__code__in=rate_codes, date__gte=checkin_date, date__lte=checkout_date)\
            .values('rate__code', 'date', 'price')
