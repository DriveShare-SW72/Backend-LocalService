from rest_framework import viewsets
from rest_framework.response import Response
from parking_app.Models.geoocodinates import Geocoordinates
from parking_app.serializers import GeocoordinatesSerializer
from drf_yasg.utils import swagger_auto_schema


class BaseGeocoordinatesViewSet(viewsets.ViewSet):
    def list(self, request): # /api/geocoordinates/
        geocoordinates = Geocoordinates.objects.all()
        serializer = GeocoordinatesSerializer(geocoordinates, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GeocoordinatesSerializer)
    def create(self, request): # /api/geocoordinates/
        serializer = GeocoordinatesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None): # /api/geocoordinates/<pk>/
        geocoordinate =  Geocoordinates.objects.get(id=pk)
        serializer = GeocoordinatesSerializer(geocoordinate)
        return Response(serializer.data)