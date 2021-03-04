from rest_framework.serializers import ModelSerializer

from roiback.models import Rate


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'name', 'code', 'room')
        read_only_fields = ('id',)
