from django.db import models
from django.conf import settings
from django.utils.functional import cached_property
from django.contrib.auth.models import User

from roiback.managers import HotelManager, RoomManager, RateManager, InventoryManager


class ModelBase(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
       abstract = True


class Hotel(ModelBase):
    code = models.CharField(max_length=20, db_index=True, unique=True)
    name = models.CharField(max_length=255)

    objects = HotelManager()

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)

    class Meta:
        db_table = '{}_model'.format(settings.APP_NAME)
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class Room(ModelBase):
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING)
    code = models.CharField(max_length=20, db_index=True, unique=True)
    name = models.CharField(max_length=255)

    objects = RoomManager()

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)

    class Meta:
        db_table = '{}_room'.format(settings.APP_NAME)
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Rate(ModelBase):
    room = models.ForeignKey(Room, models.DO_NOTHING)
    code = models.CharField(max_length=20, db_index=True, unique=True)
    name = models.CharField(max_length=255)

    objects = RateManager()

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)

    class Meta:
        db_table = '{}_rate'.format(settings.APP_NAME)
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'


class Inventory(ModelBase):
    rate = models.ForeignKey(Rate, models.DO_NOTHING)
    price = models.FloatField()
    date = models.DateField(db_index=True)

    objects = InventoryManager()

    def __str__(self):
        return '{} - {} - {} €'.format(self.rate.code, self.date, self.price)

    class Meta:
        db_table = '{}_inventory'.format(settings.APP_NAME)
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'