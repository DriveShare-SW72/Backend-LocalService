from parking_app.models import Location

class LocationService:
    def get_locations(self):
        return Location.objects.all()
    
    def create_location(self, location):
        return Location.objects.create(location)
    
    def update_location(self, location_id, new_location):
        try :
            Location.objects.filter(id= location_id).update(**new_location)
        except Location.DoesNotExist:
            return None
        return {'id': location_id, **new_location}


    def get_location_by_id(self, location_id):
        try:
            location = Location.objects.get(id = location_id)
        except Location.DoesNotExist:
            location = None
        return location


    def delete_location(self, location_id):
        try:
            Location.objects.filter(id=location_id).delete()
        except Location.DoesNotExist:
            return None
        return location_id

    

