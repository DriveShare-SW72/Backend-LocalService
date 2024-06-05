from parking_app.Models.parking_model import Parking
from django.http import JsonResponse
from parking_app.services.schedule_service import ScheduleService
from parking_app.services.location_service import LocationService
from parking_app.Enums.parking_status import ParkingStatus
from django.forms.models import model_to_dict

schedule_service = ScheduleService()
location_service = LocationService()

class ParkingService:

    def get_parkings(self):
        return Parking.objects.all()
    
    def create_parking(self, parking):
        return Parking.objects.create(**parking)
    
    def update_parking(self, parking_id, new_parking):
        try:
            Parking.objects.filter(id=parking_id).update(**new_parking)
            return {'id': parking_id, **new_parking}
        except Parking.DoesNotExist:
            return None
        
    def update_parking_status(self, parking_id, status):
        try:
            parking = Parking.objects.get(id=parking_id)
            parking.state = status
            parking.save()
            return parking
        except Parking.DoesNotExist:
            return None
        except KeyError as e:
            return None

    def delete_parking(self, parking_id):
        try:
            
            Parking.objects.filter(id=parking_id).delete()
            return parking_id
        except Parking.DoesNotExist:
            return None
    
    def get_parking_by_id(self, parking_id):
        try:
            parking = Parking.objects.get(id=parking_id)
        except Parking.DoesNotExist:
            parking = None
        
        return parking
    
    def get_parkings_by_user(self, user_id):
        parkings = Parking.objects.filter(owner_id=user_id)
        
        if not parkings.exists():
            print('No se encontraron parkings para el usuario dado.')       
        
        return parkings
    
    def get_parkings_formatted(self):
        parkings = Parking.objects.all()
        parkings_formatted = []

        for parking in parkings:
            parkings_formatted.append(self.show_parking_schedule_location(parking.pk))

        return parkings_formatted

    def show_parking_schedule_location(self, parking_id):
        parking = self.get_parking_by_id(parking_id)
        
        schedule = schedule_service.get_schedule_by_id(parking.schedule.pk)
        location = location_service.get_location_by_id(parking.location.pk)
        
        parking_dict = model_to_dict(parking)
        schedule = model_to_dict(schedule, exclude=['id'])
        location = model_to_dict(location, exclude=['id'])

        parking_dict['schedule'] = schedule
        parking_dict['location'] = location

        return parking_dict

# Tu código de vistas BaseParkingViewSet y URL patterns parece correcto, no necesita cambios
