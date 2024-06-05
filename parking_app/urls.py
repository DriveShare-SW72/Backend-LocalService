from django.contrib import admin
from django.urls import path, include
from .views import ParkingViewSet, LocationViewSet, GeocoordinatesViewSet, ScheduleViewSet
from .base_views.parking_view_set import BaseParkingViewSet
urlpatterns = [
    path('parkings', ParkingViewSet.as_view({
        'get': 'get_parkings_formatted',
        'post': 'create'
    })),
    path('parkings/<str:pk>', ParkingViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('parkings/user/<str:user_id>', ParkingViewSet.as_view({
        'get': 'get_parkings_by_user'
    })),
    path('parkings/<str:pk>/status/<str:state>/', BaseParkingViewSet.as_view({
        'put': 'update_state'
    })),
    path('locations', LocationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('locations/<str:pk>', LocationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('geocoordinates', GeocoordinatesViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('geocoordinates/<str:pk>', GeocoordinatesViewSet.as_view({
        'get': 'retrieve'
    })),
    path('schedules', ScheduleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('schedules/<str:pk>', ScheduleViewSet.as_view({
        'get': 'retrieve'
    }))
]
