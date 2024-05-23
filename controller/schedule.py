from models import Schedule


class ScheduleController:
    def __init__(self):
        self.schedule = Schedule()

    def create(self, client_id, car_id, initial_date, final_date):
        schedule, success = self.schedule.create(
            client_id=client_id,
            car_id=car_id,
            initial_date=initial_date,
            final_date=final_date
        )

        if success:
            return schedule, True
        else:
            return None, False

    def list(self):
        return self.schedule.list()

    def update(self, id, client_id, car_id, initial_date, final_date):
        schedule, success = self.schedule.update(
            id=id,
            client_id=client_id,
            car_id=car_id,
            initial_date=initial_date,
            final_date=final_date
        )

        if success:
            return schedule, True
        else:
            return None, False

    def delete(self, id):
        deleted = self.schedule.delete(id)
        if deleted:
            return True
        else:
            return False
