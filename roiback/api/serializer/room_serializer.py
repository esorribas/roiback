from rest_framework.serializers import ModelSerializer

from roiback.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'code', 'hotel_id', 'created_date')
        read_only_fields = ('id', 'created_date')
