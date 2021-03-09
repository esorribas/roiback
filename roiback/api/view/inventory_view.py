from rest_framework.viewsets import ModelViewSet

from roiback.models import Inventory
from roiback.api.serializer.inventory_serializer import InventorySerializer


class InventoryViewSet(ModelViewSet):
    serializer_class = InventorySerializer

    def get_queryset(self):
        return Inventory.objects.get_inventories()