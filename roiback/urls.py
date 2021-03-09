from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from roiback.api.view.hotel_view import HotelViewSet
from roiback.api.view.room_view import RoomViewSet
from roiback.api.view.rate_view import RateViewSet
from roiback.api.view.inventory_view import InventoryViewSet
from roiback.api.view.public_view import PublicHotelListView, PublicHotelDetailView, PublicRoomAvailabilityListView


# API Docs settings
schema_view = get_schema_view(
    openapi.Info(title='Roiback API Docs', default_version='v1'),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# DRF Routers
router = routers.DefaultRouter()

# Routers
router.register(r'hotel', HotelViewSet, basename='hotel')
router.register(r'room', RoomViewSet, basename='room')
router.register(r'rate', RateViewSet, basename='rate')
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    
    # Swagger API Docs
    re_path(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API CRUD
    re_path(r'^manage/', include(router.urls)),
    
    # Public API
    re_path(r'^api/hotels/$', PublicHotelListView.as_view({ 'get': 'list' }), name='public-hotel-list'),
    re_path(r'^api/hotels/(?P<hotel_code>[0-9a-zA-Z_-]+)/$', 
        PublicHotelDetailView.as_view({ 'get': 'retrieve' }), name='public-hotel-detail'),
    re_path(r'^api/availability/(?P<hotel_code>[0-9a-zA-Z_-]+)/(?P<checkin_date>[0-9]{4}-[0-9]{1,2}-[0-9]{1,2})/(?P<checkout_date>[0-9]{4}-[0-9]{1,2}-[0-9]{1,2})/$', 
        PublicRoomAvailabilityListView.as_view({ 'get': 'list' }), name='public-room-availability-list'),

]
