from rest_framework.serializers import ModelSerializer

from roiback.models import Inventory


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'price', 'rate_id', 'created_date')
        read_only_fields = ('id', 'created_date')
