class Car:
    def __init__(self):
        self.cars = {
            1: dict(id=1, plate='abc1234', brand='bmw', model='x6', color='branca', manufacturing_date='2024')
        }

    def create(self, plate, brand, model, color, manufacturing_date):
        id = max(self.cars.keys()) + 1 if self.cars else 1

        if not self.exists_with_this_plate(plate):
            self.cars[id] = dict(
                id=id,
                plate=plate,
                brand=brand,
                model=model,
                color=color,
                manufacturing_date=manufacturing_date
            )

            return self.cars, True

        else:
            return None, False

    def update(self, id, plate, brand, model, color, manufacturing_date):
        if not self.exists_with_this_id(id):
            return None, False

        if self.exists_with_this_plate(plate):
            return None, False

        car = self.cars[id]
        car.update(
            plate=plate,
            brand=brand,
            model=model,
            color=color,
            manufacturing_date=manufacturing_date
        )

        return car, True

    def list(self):
        return [car for _, car in self.cars.items()]

    def get_by_id(self, id):
        return self.cars.get(id)

    def delete(self, id):
        if self.exists_with_this_id(id):
            del self.cars[id]
            return True
        return False

    def exists_with_this_plate(self, plate: str) -> bool:
        for _, car in self.cars.items():
            if car['plate'] == plate:
                return True

        return False

    def exists_with_this_id(self, car_id: int) -> bool:
        return self.get_by_id(car_id) is not None
