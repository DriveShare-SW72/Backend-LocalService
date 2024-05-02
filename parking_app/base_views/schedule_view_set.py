from rest_framework import viewsets
from rest_framework.response import Response
from parking_app.models import Schedule
from parking_app.serializers import ScheduleSerializer
from drf_yasg.utils import swagger_auto_schema
from parking_app.services.schedule_service import ScheduleService

schedule_service = ScheduleService()

class BaseScheduleViewSet(viewsets.ViewSet):
    def list(self, request): # /api/schedule/
        schedules = schedule_service.get_schedules()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ScheduleSerializer)
    def create(self, request): # /api/schedule/
        serializer = ScheduleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None): # /api/schedule/<pk>/
        schedule = schedule_service.get_schedule_by_id(pk)
        
        if schedule is None:
            return Response({'message': 'Schedule not found'}, status=404)
        
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data, status=200)
    
    @swagger_auto_schema(request_body=ScheduleSerializer)
    def update(self, request, pk=None): # /api/schedule/<pk>/
        new_schedule = schedule_service.update_schedule(pk, request.data)
        if new_schedule is None:
            return Response({'message': 'Schedule not found'}, status=404)
        serializer = ScheduleSerializer(new_schedule)
        return Response(serializer.data, status=200)
    
    def destroy(self, request, pk=None): # /api/schedule/<pk>/
        schedule_id = schedule_service.delete_schedule(pk)
        if schedule_id is None:
            return Response({'message': 'Schedule not found'}, status=404)
        return Response({'message': f'Schedule with ID {schedule_id} deleted successfully'}, status=200)
    