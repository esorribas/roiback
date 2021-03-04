from rest_framework.serializers import BaseSerializer, ModelSerializer

from roiback.models import Hotel


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'code')
        read_only_fields = ('id',)


class HotelAvailabilitySerializer(BaseSerializer):
    def to_representation(self, instance):
        return {
            'rooms': instance.score,
            'player_name': instance.player_name
        }

"""
class CustomSerializer(serializers.Serializer):
    ...
    class Meta:
        list_serializer_class = HotelAvailabilitySerializer"""