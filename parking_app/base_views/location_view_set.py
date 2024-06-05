from rest_framework import viewsets 
from rest_framework.response import Response

# Create your views here.
from parking_app.serializers import LocationSerializer
from parking_app.Models.location_model import Location
from parking_app.services.location_service import LocationService

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

location_service = LocationService()

class BaseLocationViewSet(viewsets.ViewSet):
    def list(self, request): # /api/locations/
        locations = location_service.get_locations()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LocationSerializer)
    def create(self, request): # /api/locations/
        serializer = LocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk): # /api/locations/<pk>/
        location =  location_service.get_location_by_id(pk)
        
        if location is None:
            return Response({'message': 'Location not found'}, status=404)

        serializer = LocationSerializer(location)
        
        return Response(serializer.data, status=200)
    
    @swagger_auto_schema(request_body=LocationSerializer)
    def update(self, request, pk=None):
        new_location= location_service.update_location(pk, request.data)
        if new_location is None:
            return Response({'message': 'Location not found'}, status=404)
        serializer = LocationSerializer(new_location)
        return Response(serializer.data, status=200)
    
    def destroy(self, request, pk=None):
        location_id = location_service.delete_location(pk)
        if location_id is None:
            return Response({'message': 'Location not found'}, status=404)
  
        return Response({'message': f'Location with ID {location_id} deleted successfully'}, status=200)
