from controller import CarController
from controller import ClientController
from controller import ScheduleController

car_controller = CarController()
client_controller = ClientController()
schedule_controller = ScheduleController()

cars = car_controller.list()
clients = client_controller.list()
schedules = schedule_controller.list()

def verify_empty_dict(type: str) -> bool:
    if type == "cars":
        if not cars:
            return True
    elif type == "clients":
        if not clients:
            return True
    elif type == "schedules":
        if not schedules:
            return True
    return False
