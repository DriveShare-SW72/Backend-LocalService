# Create your views here.
from .base_views.parking_view_set import BaseParkingViewSet
from .base_views.location_view_set import BaseLocationViewSet
from .base_views.geoocordinates_view_set import BaseGeocoordinatesViewSet
from .base_views.schedule_view_set import BaseScheduleViewSet
from .base_views.review_view_set import BaseReviewViewSet


# Create your views here.

class ParkingViewSet(BaseParkingViewSet):
    pass
    
class LocationViewSet(BaseLocationViewSet):
    pass 

class GeocoordinatesViewSet(BaseGeocoordinatesViewSet):
    pass

class ScheduleViewSet(BaseScheduleViewSet):
    pass
    
class ReviewViewSet(BaseReviewViewSet):
    pass