from rest_framework.serializers import ModelSerializer

from roiback.models import Rate


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'name', 'code', 'room_id', 'created_date')
        read_only_fields = ('id', 'created_date')
