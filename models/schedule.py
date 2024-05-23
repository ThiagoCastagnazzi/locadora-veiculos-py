from models import Car
from models import Client

client_model = Client()
car_model = Car()


class Schedule:
    def __init__(self):
        self.schedules = {}

    def create(self, client_id, car_id, initial_date, final_date):
        if not client_model.get_by_id(client_id):
            return None, False

        if not car_model.exists_with_this_id(car_id):
            return None, False

        id = max(self.schedules.keys()) + 1 if self.schedules else 1

        self.schedules[id] = dict(
            id=id,
            client_id=client_id,
            car_id=car_id,
            initial_date=initial_date,
            final_date=final_date
        )

        return self.schedules, True

    def list(self):
        schedule_list = []
        for _, schedule in self.schedules.items():
            client_id = schedule['client_id']
            car_id = schedule['car_id']

            client = client_model.get_by_id(client_id)
            car = car_model.get_by_id(car_id)

            if car and client:
                schedule['client_cpf'] = client['cpf']
                schedule['car_plate'] = car['plate']

                schedule_list.append(schedule)

        return schedule_list

    def update(self, id, client_id, car_id, initial_date, final_date):
        if not client_model.get_by_id(client_id):
            return None, False

        if not car_model.exists_with_this_id(car_id):
            return None, False

        schedule = self.schedules[id]
        schedule.update(
            id=id,
            client_id=client_id,
            car_id=car_id,
            initial_date=initial_date,
            final_date=final_date
        )

        return schedule, True

    def delete(self, id):
        if self.exists_with_this_id(id):
            del self.schedules[id]
            return True
        else:
            return False

    def exists_with_this_id(self, schedule_id: int) -> bool:
        for _, schedule in self.schedules.items():
            if schedule['id'] == schedule_id:
                return True

        return False
