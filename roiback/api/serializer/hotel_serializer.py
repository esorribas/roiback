from rest_framework.serializers import ModelSerializer

from roiback.models import Hotel


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'code')
        read_only_fields = ('id',)
