from rest_framework.serializers import ModelSerializer

from roiback.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'code', 'hotel')
        read_only_fields = ('id',)
