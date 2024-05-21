from controller import CarController
from controller import ClientController

schedules = {}

car_controller = CarController()
client_controller = ClientController()

class ScheduleController:
    def exists_with_this_id(self, schedule_id: int) -> bool:
        for _, schedule in schedules.items():
            if schedule['id'] == schedule_id:
                return True

        return False

    def create(self, client_id, car_id, initial_date, final_date):
        if schedules:
            id = max(schedules.keys()) + 1
        else:
            id = 1

        schedules[id] = dict(
            id=id,
            client_id=client_id,
            car_id=car_id,
            initial_date=initial_date,
            final_date=final_date
        )

    def list(self):
        schedule_list = []
        for _, schedule in schedules.items():
            client_id = schedule['client_id']
            car_id = schedule['car_id']

            client = client_controller.exists_with_this_id(client_id)

            car = car_controller.get_by_id(car_id)

            if car and client:
                schedule['client_cpf'] = client['cpf']
                schedule['car_plate'] = car['plate']

                schedule_list.append(schedule)

        return schedule_list

    def update(self, id, client_id, car_id, initial_date, final_date):
        schedules[id] = dict(
            id=id,
            client_id=client_id,
            car_id=car_id,
            initial_date=initial_date,
            final_date=final_date
        )

    def delete(self, id):
        del schedules[id]
