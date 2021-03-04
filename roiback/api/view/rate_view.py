from rest_framework.viewsets import ModelViewSet

from roiback.models import Rate
from roiback.api.serializer.rate_serializer import RateSerializer


class RateViewSet(ModelViewSet):
    serializer_class = RateSerializer

    def get_queryset(self):
        return Rate.objects.order_by('-created_date')
