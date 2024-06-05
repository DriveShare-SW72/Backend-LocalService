# Create your views here.
from .base_views.parking_view_set import BaseParkingViewSet
from .base_views.location_view_set import BaseLocationViewSet
from .base_views.geoocordinates_view_set import BaseGeocoordinatesViewSet
from .base_views.schedule_view_set import BaseScheduleViewSet
from .base_views.review_view_set import BaseReviewViewSet

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


class ParkingViewSet(BaseParkingViewSet):
    permission_classes = [AllowAny]


class LocationViewSet(BaseLocationViewSet):
    permission_classes = [AllowAny]


class GeocoordinatesViewSet(BaseGeocoordinatesViewSet):
    permission_classes = [AllowAny]


class ScheduleViewSet(BaseScheduleViewSet):
    permission_classes = [AllowAny]

    
class ReviewViewSet(BaseReviewViewSet):
    permission_classes = [AllowAny]
