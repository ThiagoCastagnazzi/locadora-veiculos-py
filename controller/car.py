from models import Car


class CarController:
    def __init__(self):
        self.car = Car()

    def create(self, plate, brand, model, color, manufacturing_date):
        car, success = self.car.create(
            plate=plate,
            brand=brand,
            model=model,
            color=color,
            manufacturing_date=manufacturing_date
        )

        if success:
            return car, True
        else:
            return None, False

    def list(self):
        return self.car.list()

    def get_by_id(self, id):
        return self.car.get_by_id(id=id)

    def update(self, id, plate, brand, model, color, manufacturing_date):
        car, success = self.car.update(
            id=id,
            plate=plate,
            brand=brand,
            model=model,
            color=color,
            manufacturing_date=manufacturing_date
        )

        if success:
            return car, True
        else:
            return None, False

    def delete(self, id):
        deleted = self.car.delete(id=id)
        if deleted:
            return True
        else:
            return False
