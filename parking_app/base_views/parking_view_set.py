# Create your views here.
from parking_app.serializers import ParkingSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from django.http import JsonResponse
from parking_app.serializers import ParkingSerializer
from parking_app.services.parking_service import ParkingService 
from parking_app.Models.parking_model import ParkingStatus
parking_service = ParkingService()

class BaseParkingViewSet(viewsets.ViewSet):
    def list(self, request): # /api/parking/
        parkings = parking_service.get_parkings()
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ParkingSerializer)
    def create(self, request): # /api/parking/
        serializer = ParkingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


    def update_state(self, request, pk=None, state=None):
        new_status = parking_service.update_parking_status(pk, state)
        state = getattr(ParkingStatus, state.upper(), None)
        if state is None:
            possible_values = [s.value for s in ParkingStatus]
            return Response({'message': f'Invalid status: {state}. Possible values are: {", ".join(possible_values)}'}, status=status.HTTP_400_BAD_REQUEST)
        if new_status is None:
            return Response({'message': 'Parking not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'State updated successfully'})

    def retrieve(self, request, pk=None): # /api/parking/<pk>/
        parking = parking_service.get_parking_by_id(pk)
        
        if parking is None:
            return Response({'message': 'Parking not found'}, status=404)
        

        serializer = ParkingSerializer(parking)

        return Response(serializer.data, status=200)

    @swagger_auto_schema(request_body=ParkingSerializer)
    def update(self, request, pk=None): # /api/parking/<pk>/
        new_parking = parking_service.update_parking(pk, request.data)
        if new_parking is None:
            return Response({'message': 'Parking not found'}, status=404)
        serializer = ParkingSerializer(new_parking)
        return Response(serializer.data, status=200)

    def destroy(self, request, pk=None): # /api/parking/<pk>/
        parking_id = parking_service.delete_parking(pk)
        if parking_id is None:
            return Response({'message': 'Parking not found'}, status=404)

        return Response({'message': f'Parking with ID {parking_id} deleted successfully'}, status=200)
    
    def get_parkings_by_user(self, request, user_id):
        parking_service = ParkingService()
        parkings = parking_service.get_parkings_by_user(user_id)

        serializer = ParkingSerializer(parkings, many=True)
        
        parkings_data = [{'id': item['id'], 'description': item['description'], 'address': item['address'], 'city': item['city']} for item in serializer.data]
        
        return JsonResponse(parkings_data, safe=False)
    
    def get_parkings_formatted(self, request):
        parkings = parking_service.get_parkings_formatted()
        return Response(parkings, status = 200)
    

