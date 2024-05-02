from parking_app.models import Schedule

class ScheduleService:
    def get_schedules(self):
        return Schedule.objects.all()
    
    def create_schedule(self, schedule):
        return Schedule.objects.create(schedule)
    
    def update_schedule(self, schedule_id, new_schedule):
        try:
            Schedule.objects.filter(id=schedule_id).update(**new_schedule)
            return {'id': schedule_id, **new_schedule}
        except Schedule.DoesNotExist:
            return None
        
    def delete_schedule(self, schedule_id):
        try:
            Schedule.objects.filter(id=schedule_id).delete()
            return schedule_id
        except Schedule.DoesNotExist:
            return None
        
    def get_schedule_by_id(self, schedule_id):
        try:
            schedule = Schedule.objects.get(id = schedule_id)
        except Schedule.DoesNotExist:
            schedule = None
        
        return schedule
    

